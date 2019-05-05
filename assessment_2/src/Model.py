"""
Model.py
A python script containing a model with which to test the Ensemble Kalman Filter
@author: ksuchak1990
"""

# Imports
import numpy as np

# Car Model
class Car_Model():
    def __init__(self, model_params):
        """
        Initialise the model with model parameters.
        """
        # Set params to default values if not provided in model_params.
        self.required_model_params = {'x_speed': 5,
                                      'y_speed': 5,
                                      'noise_mean': 0,
                                      'noise_std': 0}

        for k, v in self.required_model_params.items():
            if k in model_params:
                setattr(self, k, model_params[k])
            else:
                setattr(self, k, v)

        # Initial state
        self.time_step = 1
        self.time = 0
        self.state = np.array([0, 0])

        # Collecting states
        self.times = [self.time]
        self.states = [self.state.copy()]
