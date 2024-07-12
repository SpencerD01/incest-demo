from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from target import Target
import numpy as np

# Define our target function.
t1 = Target(2., 0.1)

# Create a Kalman Filter
kf = KalmanFilter(dim_x=2, dim_z=1)

# Assign the initial values for the state (position and velocity).
kf.x = np.array([2., 0.])

# Define the state transition matrix.
kf.F = np.array([[1., 1.],
                 [0., 1.]])

# Define the measurement function.
kf.H = np.array([[1., 0.]])

# Define the covariance matrix.
kf.P = np.array([[1000.,    0.],
                 [   0., 1000.]])

# Define the measurement noise.
kf.R = np.array([5.])

# Define the process noise.
kf.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)

