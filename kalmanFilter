import pandas as pd
import numpy as np
from pykalman import KalmanFilter

import matplotlib.pyplot as plt


plt.style.use('seaborn-darkgrid')
plt.rcParams['figure.figsize'] = (10,7)
df1 = pd.read_csv('test.csv')
kf = KalmanFilter(transition_matrices = [1],
              observation_matrices = [1],
              initial_state_mean = 20,
              initial_state_covariance = 1,
              observation_covariance=24.293,
              transition_covariance=4.017)

measured=np.array(df1['Measured_dis'])
real=np.array(df1['Real_dis'])
filtered, cov = kf.filter(measured)
filtered, std = filtered.squeeze(), np.std(cov.squeeze())

plt.figure(figsize=(15,7))
plt.plot(measured, 'g', lw=1)
plt.plot(filtered, 'r', lw=1)
plt.plot(real, 'c', lw=1)
plt.title('Kalman filter in test')
plt.legend(['measured', 'filtered', 'real'])
plt.xlabel('number')
plt.ylabel('Distance')
plt.show()

old_noise=np.array(measured-real)
new_noise=np.array(filtered-real)

old_var=np.std(old_noise)
print("old noise:",old_var)
new_var=np.std(new_noise)
print("new noise:",new_var)
