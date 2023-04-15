
# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Parse user's arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('-amplitude', type=float, default=1.0,
                     help="Amplitude of function sin()")
parser.add_argument('-initial_angle', type=float, default=0.0, 
                     help="Initial angle where the function sin() will be evaluated")
parser.add_argument('-final_angle', type=float, default=6.28, 
                     help="Final angle where the function sin() will be evaluated")
parser.add_argument('-n_samples', type=int, default=1000, 
                     help="number of samples bewteen initial_angle and final_angle")
args = parser.parse_args()


# Initialise a numpy-type list
theta = np.linspace(start=args.initial_angle, stop=args.final_angle, num=args.n_samples)

# Evaluate the function 'sin' on 'x'
y = args.amplitude * np.sin(theta)

# Visualise the function 'y = sin(x)'
plt.figure(1)
plt.plot(theta,y,linewidth=2)
plt.title(r"Function $y=\sin(\theta)$ ")
plt.xlabel(r"$\theta$")
plt.ylabel("y")
plt.show()




