import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0.3], [0]])

theta_init = np.deg2rad(134)

R = np.array([[np.cos(theta_init), -np.sin(theta_init)],[np.sin(theta_init), np.cos(theta_init)]])

x1 = np.matmul(R, x)

print(x1)

plt.scatter(x1[0], x1[1])
plt.grid()
plt.show()