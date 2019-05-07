"""
EnsembleKalmanFilter.py
A python script containing an implementation of the Ensemble Kalman Filter.
@author: ksuchak1990
"""

# Imports
import warnings as warns
import numpy as np

# Class
class EnsembleKalmanFilter:
    """
    A class to represent a general Ensemble Kalman Filter (EnKF).
    """
    def __init__(self, model, filter_params, model_params):
        """
        Initialise the EnKF.

        Params:
            model
            filter_params
            model_params

        Returns:
            None
        """

        self.time = 0

        # Ensure that model has correct attributes
        # We would also like to make sure that step is callable
        if not hasattr(model, 'step'):
            raise AttributeError("Model has no 'step' method.")
        if not callable(model.step):
            raise AttributeError("Model 'step' is not callable.")

        # Filter attributes - outlines the expected params
        self.max_iterations = None
        self.ensemble_size = None
        self.state_vector_length = None
        self.data_vector_length = None
        self.H = None
        self.R_vector = None
        self.data_covariance = None

        # Get filter attributes from params, warn if unexpected attribute
        for k, v in filter_params.items():
            if not hasattr(self, k):
                w = 'EnKF received unexpected {0} attribute.'.format(k)
                warns.warn(w, RuntimeWarning)
            setattr(self, k, v)

        # Set up ensemble of models
        self.models = [model(model_params) for _ in range(self.ensemble_size)]

        # Make sure that models have state
        for m in self.models:
            if not hasattr(m, 'state'):
                raise AttributeError("Model has no 'state' attribute.")
        
        # We're going to nee H.T very often, so just do it once and store
        self.H_transpose = self.H.T

        # Make sure that we have a data covariance matrix
        if not self.data_covariance:
            self.data_covariance = np.diag(self.R_vector)

        # Create placeholders for ensembles
        self.state_ensemble = np.zeros(shape=(self.state_vector_length,
                                              self.ensemble_size))
        self.state_mean = None
        self.data_ensemble = np.zeros(shape=(self.data_vector_length,
                                             self.ensemble_size))

        self.update_state_ensemble()
        self.update_state_mean()
        self.results = [self.state_mean]

    def step(self, data=None):
        """
        Step the filter forward by one time-step.

        Params:
            data

        Returns:
            None
        """
        self.predict()
        self.update_state_ensemble()
        self.update_state_mean()
        
        if not data is None:
            self.update(data)
            self.update_models()
        self.time += 1
        self.update_state_mean()
        self.results.append(self.state_mean)

    def predict(self):
        """
        Step the models forward by one time-step to produce predictions
        
        Params:
            None

        Returns
            None
        """
        for i in range(self.ensemble_size):
            self.models[i].step()

    def update(self, data):
        """
        Update  filter with data provided.

        Params:
            data

        Returns:
            None
        """
        # Make sure that provided data is correct length
        if len(data) != self.data_vector_length:
            w = 'len(data)={0}, expected {1}'.format(len(data),
                                                     self.data_vector_length)
            warns.warn(w, RuntimeWarning)

        X = np.zeros(shape=(self.state_vector_length, self.ensemble_size))
        gain_matrix = self.make_gain_matrix()
        self.update_data_ensemble(data)

        for i in range(self.ensemble_size):
            diff = self.data_ensemble[:, i] - self.H @ self.state_ensemble[:, i]
            X[:, i] = self.state_ensemble[:, i] + gain_matrix @ diff
        self.state_ensemble = X

    def update_state_ensemble(self):
        """
        Update self.state_ensemble based on the state of the models.
        """
        for i in range(self.ensemble_size):
            self.state_ensemble[:, i] = self.models[i].state

    def update_state_mean(self):
        """
        Update self.state_mean based on current state ensemble.
        """
        self.state_mean = np.mean(self.state_ensemble, axis=1)

    def update_data_ensemble(self, data):
        """
        Create ensemble of perturbed data vectors.
        I.e. replicates of the data vector plus a normal random n-d vector.
        R - data covariance; this should be either
            i) a number, or
            ii) a vector with same length as the data.
        """
        x = np.zeros(shape=(len(data), self.ensemble_size))
        for i in range(self.ensemble_size):
            x[:, i] = data + np.random.normal(0, self.R_vector, len(data))
        self.data_ensemble = x

    def update_models(self):
        """
        Update individual model states based on state ensemble.
        """
        for i in range(self.ensemble_size):
            self.models[i].state = self.state_ensemble[:, i]

    def make_ensemble_covariance(self):
        """
        Create ensemble covariance matrix.
        """
        a = self.state_ensemble @ np.ones(shape=(self.ensemble_size, 1))
        b = np.ones(shape=(1, self.ensemble_size))
        A = self.state_ensemble - 1/self.ensemble_size * a @ b
        return 1/(self.ensemble_size - 1) * A @ A.T

    def make_gain_matrix(self):
        """
        Create kalman gain matrix.
        """
        C = np.cov(self.state_ensemble)
        state_covariance = self.H @ C @ self.H_transpose
        diff = state_covariance - self.data_covariance
        return C @ self.H_transpose @ np.linalg.inv(diff)


