import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

data = np.genfromtxt(
    'zephyrus_testlaunch_OR_output_noAirbrakes.csv',
    delimiter=',',
    skip_header=1
)

t_unmask = data[:, 0] 
alt_unmask = data[:, 1]
vel_unmask = data[:, 2]
vel_mag_unmask = data[:, 3]
accel_unmask = data[:, 4]

mask = (t_unmask > 12) & (vel_unmask > 343)
t = t_unmask[~mask]
alt = alt_unmask[~mask]
vel = vel_unmask[~mask]
vel_mag = vel_mag_unmask[~mask]
accel = accel_unmask[~mask]

# Plotting 
plt.plot(t, alt, label='Altitude (m)', color='blue')
plt.plot(t, vel, label='Velocity (m/s)', color='green')
# plt.plot(t, accel, label='Acceleration (m/s²)')
ax = plt.gca()
ax.set_ylim(0, 6500)
ax2 = ax.twinx()
ax2.plot(t, accel, label='Acceleration (m/s²)', color='purple')

plt.show()
