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
MODEL_NOISE_STD = 20
OBS_NOISE_MEAN = 0
OBS_NOISE_STD = 20
ASSIMILATION_PERIOD = 10

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

filter_params = {'max_iterations': N_STEPS,
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

# Plotting functions
def plot_positions(x, y):
    """
    Plotting function to compare enkf model state with truth and obs.
    """
    plt.figure()
    plt.plot(true_x, true_y, '--b', label='truth')
    plt.scatter(obs_x, obs_y, color='black', alpha=0.5, label='obs')
    plt.scatter(x, y, color='red', alpha=0.5, label='model')
    plt.title('$\sigma_o={0}$, $\sigma_m={1}$'.format(OBS_NOISE_STD,
                                                      MODEL_NOISE_STD))
    plt.legend()
    plt.show()

def plot_errors(x, y):
    """
    Plotting function to visualise error of filter.
    """
    x_model_error = [np.abs(x[i] - true_x[i]) for i in range(len(true_x))]
    y_model_error = [np.abs(y[i] - true_y[i]) for i in range(len(true_y))]

    plt.figure()
    data = [x_model_error, y_model_error]
    plt.boxplot(data)
    plt.xlabel('Axis')
    plt.ylabel('Absolute error')
    plt.show()

plot_positions(model_x, model_y)
plot_errors(model_x, model_y)

def test_enkf(n, t):
    """
    Function to test the ensemble kalman filter for a given ensemble size.
    """
    print('Running for ensemble_size={0}, period={1}'.format(n, t))
    model_params = {'x_speed': CAR_X_SPEED,
                    'y_speed': CAR_Y_SPEED,
                    'noise_mean': MODEL_NOISE_MEAN,
                    'noise_std': MODEL_NOISE_STD}
    filter_params = {'max_iterations': N_STEPS,
                     'ensemble_size': n,
                     'state_vector_length': 2,
                     'data_vector_length': 2,
                     'H': np.identity(2),
                     'R_vector': np.array([OBS_NOISE_STD, OBS_NOISE_STD])}
    
    e = EnKF(Car_Model, filter_params, model_params)

    # Step filter
    for i in range(N_STEPS):
        if i % t == 0:
            observation = np.array([obs_x[i], obs_y[i]])
            e.step(observation)
        else:
            e.step()

    # Get model outputs
    model_x = [state[0] for state in e.results]
    model_y = [state[1] for state in e.results]

    # Plotting
    plot_positions(model_x, model_y)
    plot_errors(model_x, model_y)

def runner():
    sizes = [10, 20, 50, 100]
    periods = [10, 20, 50]
    for n in sizes:
        for t in periods:
            test_enkf(n, t)

runner()
