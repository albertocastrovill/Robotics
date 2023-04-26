# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--num_links', type=int,default=2, help=" Number of Links of the Robotic Arm")
parser.add_argument('--iters', type=int,default=100, help=" Iterations")
parser.add_argument('--mean_a', type=float, nargs='+',default=0.0, help="Mean A")
parser.add_argument('--std_a', type=float,default=0.1, help="Standard Deviation A")
parser.add_argument('--mean_theta', type=int, nargs='+',default=0, help="Mean Theta")
parser.add_argument('--std_theta', type=float,default=0.1, help="Standard Deviation Theta")

args = parser.parse_args()

# Define uncertainties associated to joints and links
mean_a1, std_a1 = args.mean_a[0], args.std_a
mean_theta1, std_theta1 = args.mean_theta[0], args.std_theta
mean_a2, std_a2 = args.mean_a[1], args.std_a
mean_theta2, std_theta2 = args.mean_theta[1], args.std_theta
mean_a3, std_a3 = args.mean_a[2], args.std_a
mean_theta3, std_theta3 = args.mean_theta[2], args.std_theta
 
# Define two arrays to hold the joints positions
NITERS = args.iters
J1_G_samples = np.zeros((2, NITERS))
J2_G_samples = np.zeros((2, NITERS))
J3_G_samples = np.zeros((2, NITERS))

# Main loop
for i in range(NITERS):
	
	# Sample a1 and theta1 from a Gaussian PDF
	a1 = np.random.normal(loc=mean_a1, scale=std_a1)
	theta1 = np.deg2rad(np.random.normal(loc=mean_theta1, scale=std_theta1))

	# Compute the position of Joint 1
	T1 = np.array([[np.cos(theta1), -np.sin(theta1), a1*np.cos(theta1)], 
				  [ np.sin(theta1),  np.cos(theta1), a1*np.sin(theta1)],
				  [ 0             ,  0             , 1               ]])
	J1 = np.array([[0], [0], [1]])
	J1_G = np.dot(T1, J1)
	J1_G_samples[:,i] = J1_G[0:2,0]

	# Sample a2 and theta2 from a Gaussian PDF
	a2 = np.random.normal(loc=mean_a2, scale=std_a2)
	theta2 = np.deg2rad(np.random.normal(loc=mean_theta2, scale=std_theta2))

	# Compute the position of Joint 2
	T2 = np.array([[np.cos(theta2), -np.sin(theta2), a2*np.cos(theta2)], 
				  [ np.sin(theta2),  np.cos(theta2), a2*np.sin(theta2)],
				  [ 0             ,  0             , 1               ]])
	J2 = np.array([[0], [0], [1]])
	J2_G = np.dot(T1, np.dot(T2, J2))
	J2_G_samples[:,i] = J2_G[0:2,0]

	# Sample a3 and theta3 from a Gaussian PDF
	a3 = np.random.normal(loc=mean_a3, scale=std_a3)
	theta3 = np.deg2rad(np.random.normal(loc=mean_theta3, scale=std_theta3))

	# Compute the position of Joint 3
	T3 = np.array([[np.cos(theta3), -np.sin(theta3), a3*np.cos(theta3)], 
				  [ np.sin(theta3),  np.cos(theta3), a3*np.sin(theta3)],
				  [ 0             ,  0             , 1               ]])
	J3 = np.array([[0], [0], [1]])
	J3_G = np.dot(T2, np.dot(T3, J3))
	J3_G_samples[:,i] = J3_G[0:2,0]


# Compute mean of each error data points
mean_J1 = np.mean(J1_G_samples, axis=1)
mean_J2 = np.mean(J2_G_samples, axis=1)
mean_J3 = np.mean(J3_G_samples, axis=1)

print(mean_J1)
print(mean_J2)
print(mean_J3)

# Visualise the error propagation
plt.figure(1, figsize=(6,6))
plt.scatter(0, 0, s=20)

plt.scatter(J1_G_samples[0,:], J1_G_samples[1,:], s=5)
plt.plot([0, mean_J1[0]], [0, mean_J1[1]], 'b', linewidth=2)

plt.scatter(J2_G_samples[0,:], J2_G_samples[1,:], s=5)
plt.scatter(mean_J2[0], mean_J2[1], s=20, color='r', linewidth=2)

plt.scatter(J3_G_samples[0,:], J3_G_samples[1,:], s=5)
plt.scatter(mean_J3[0], mean_J3[1], s=10, color='g')

plt.plot([mean_J1[0], mean_J2[0]], [mean_J1[1], mean_J2[1]], 'b', linewidth=2)
plt.plot([mean_J2[0], mean_J3[0]], [mean_J2[1], mean_J3[1]], 'b', linewidth=2)
plt.axis('equal')
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 2])
plt.show()

#if __name__ == "__main__":
