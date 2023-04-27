# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--num_links', type=int,default=1, help=" Number of Links of the Robotic Arm")
parser.add_argument('--iters', type=int,default=100, help=" Iterations")
parser.add_argument('--mean_a', type=int, nargs='+',default=0, help="Mean A")
parser.add_argument('--std_a', type=float, nargs='+',default=0.1, help="Standard Deviation A")
parser.add_argument('--mean_theta', type=int, nargs='+',default=0, help="Mean Theta")
parser.add_argument('--std_theta', type=float, nargs='+',default=0.1, help="Standard Deviation Theta")

args = parser.parse_args()


def variable_init():
    global mean_a, std_a, mean_theta, std_theta, NITERS, J_G_samples

    # Define uncertainties associated to joints and links
    mean_a, std_a = args.mean_a, args.std_a
    mean_theta, std_theta = args.mean_theta, args.std_theta

    # Define an array to hold the joints positions
    NITERS = args.iters
    J_G_samples = np.zeros((2 * args.num_links, NITERS))


def calculate_joint_positions(num_links, mean_a, std_a, mean_theta, std_theta):
    # initialize arrays for joint positions
    joint_positions = np.zeros((2, num_links))

    # initialize transformation matrix and joint vector
    T = np.eye(3)
    J = np.array([[0], [0], [1]])

    for i in range(num_links):
        # Sample a and theta from a Gaussian PDF
        a = np.random.normal(loc=mean_a[i], scale=std_a[i])
        theta = np.deg2rad(np.random.normal(loc=mean_theta[i], scale=std_theta[i]))

        # Compute the position of the current joint
        T_i = np.array([[np.cos(theta), -np.sin(theta), a*np.cos(theta)], 
                        [np.sin(theta), np.cos(theta), a*np.sin(theta)],
                        [0, 0, 1]])
        T = np.dot(T, T_i)
        J_G = np.dot(T, J)
        joint_positions[:,i] = J_G[0:2,0]

    return joint_positions


if __name__ == "__main__":
    variable_init()
    # Main loop
    for i in range(NITERS):
        
        # Compute the position of each joint
        joint_positions = calculate_joint_positions(3, mean_a, std_a, mean_theta, std_theta)
        

    # Compute mean of each error data points
    mean_J = np.mean(J_G_samples, axis=1)

    # Visualise the error propagation
    plt.figure(1, figsize=(10,10))
    plt.scatter(0, 0, s=20)

    for j in range(args.num_links):
        plt.scatter(J_G_samples[j,0,:], J_G_samples[j,1,:], s=5)
        plt.plot([0, mean_J[j,0]], [0, mean_J[j,1]], linewidth=2)

    #plt.plot([mean_J1[0], mean_J2[0]], [mean_J1[1], mean_J2[1]], 'b', linewidth=2)
    plt.axis('equal')
    plt.xlim([-40, 100])
    plt.ylim([-40, 100])
    plt.show()

