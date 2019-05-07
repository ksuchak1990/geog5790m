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

    def step(self):
        """
        Step model forward one step in time.
        """
        # Calculate updates
        x_noise = np.random.normal(self.noise_mean, self.noise_std)
        y_noise = np.random.normal(self.noise_mean, self.noise_std)
        x_update = self.x_speed * self.time_step + x_noise
        y_update = self.y_speed * self.time_step + y_noise

        # Update state and time
        self.time += self.time_step
        self.state[0] += x_update
        self.state[1] += y_update

        # Add to list of states
        self.times.append(self.time)
        self.states.append(self.state.copy())

