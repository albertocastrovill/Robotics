import numpy as np
import matplotlib.pyplot as plt
import argparse

# Parse
parser = argparse.ArgumentParser()

parser.add_argument('--amplitude', type=int, nargs='+',default=1.0, help=" 3 Amplitudes")

args = parser.parse_args()

theta = np.arange(0,2*np.pi,0.01)

y = np.sin(theta)

for amp in args.amplitude:
    plt.plot(theta, amp*y)


plt.xlabel(r"$\theta$")
plt.ylabel(r"y($\theta$)")
plt.show()
