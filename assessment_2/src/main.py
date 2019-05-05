"""
main.py
A python script to test out the Ensemble Kalman Filter with a basic model.
@author: ksuchak1990
"""

# Imports
import matplotlib.pyplot as plt
from Model import Car_Model

# Constants
CAR_X_SPEED = 5
CAR_Y_SPEED = 5
N_STEPS = 100
MODEL_NOISE_MEAN = 0
MODEL_NOISE_STD = 10

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
