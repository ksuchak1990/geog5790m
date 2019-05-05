"""
main.py
A python script to test out the Ensemble Kalman Filter with a basic model.
@author: ksuchak1990
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
from Model import Car_Model
from EnsembleKalmanFilter import EnsembleKalmanFilter as EnKF

# Set seed for reproducibility
np.random.seed(666)

# Constants
CAR_X_SPEED = 5
CAR_Y_SPEED = 5
N_STEPS = 100
MODEL_NOISE_MEAN = 0
MODEL_NOISE_STD = 10
OBS_NOISE_MEAN = 0
OBS_NOISE_STD = 10
ASSIMILATION_PERIOD = 5

def make_data(params, n, vis=True):
    """
    A function to create data from the model.
    """
    cm = Car_Model(params)
    for i in range(n):
        cm.step()

    # Get model state as lists
    x = [state[0] for state in cm.states]
    y = [state[1] for state in cm.states]
    times = cm.times

    # Check data with plot
    if vis:
        plt.figure()
        plt.scatter(x, y)
        plt.xlabel('Car x-position')
        plt.ylabel('Car y-position')
        plt.show()

    return x, y, times

# Use model to make 'truth' data
track_params = {'x_speed': CAR_X_SPEED,
                'y_speed': CAR_Y_SPEED,
                'noise_mean': 0,
                'noise_std': 0}

true_x, true_y, true_times = make_data(track_params, N_STEPS)

# Use model to make 'observation' data
obs_params = {'x_speed': CAR_X_SPEED,
              'y_speed': CAR_Y_SPEED,
              'noise_mean': 0,
              'noise_std': 0}

obs_x, obs_y, obs_times = make_data(obs_params, N_STEPS, vis=False)

# Add noise to observations
obs_x = [x + np.random.normal(OBS_NOISE_MEAN, OBS_NOISE_STD) for x in obs_x]
obs_y = [y + np.random.normal(OBS_NOISE_MEAN, OBS_NOISE_STD) for y in obs_y]

plt.figure()
plt.scatter(obs_x, obs_y)
plt.xlabel('Observed car x-position')
plt.ylabel('Observed car y-position')
plt.show()

# Set up EnKF
model_params = {'x_speed': CAR_X_SPEED,
                'y_speed': CAR_Y_SPEED,
                'noise_mean': MODEL_NOISE_MEAN,
                'noise_std': MODEL_NOISE_STD}

filter_params = {'max_iterations': 50,
                 'ensemble_size': 100,
                 'state_vector_length': 2,
                 'data_vector_length': 2,
                 'H': np.identity(2),
                 'R_vector': np.array([OBS_NOISE_STD, OBS_NOISE_STD])}

# Initialise filter with car model
e = EnKF(Car_Model, filter_params, model_params)

# Step filter
for i in range(N_STEPS):
    if i % ASSIMILATION_PERIOD == 0:
        observation = np.array([obs_x[i], obs_y[i]])
        e.step(observation)
    else:
        e.step()

model_x = [state[0] for state in e.results]
model_y = [state[1] for state in e.results]

