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

def calculate_joints_position(a, theta):
    # Compute the position of Joint 1
    joints_positions = np.zeros((3, args.num_links))
    J = np.array([[0], [0], [1]])
    #J = np.array([[0, 0,1]])
    for i in range(args.num_links):
        T_i = np.array([[np.cos(theta[i]), -np.sin(theta[i]), a[i]*np.cos(theta[i])], 
                        [np.sin(theta[i]), np.cos(theta[i]), a[i]*np.sin(theta[i])],
                        [0, 0, 1]])
        print(T_i)
        #joints_positions[:, i] = np.dot(T_i, J)
        joints_positions[:, i] = np.dot(T_i, J)
    J_G = joints_positions[:2, :].reshape(-1, order='F')
    
    return J_G


if __name__ == "__main__":
    variable_init()
    # Main loop
    for i in range(NITERS):
        # Sample a and theta values from a Gaussian PDF
        a = np.random.normal(loc=mean_a, scale=std_a, size=args.num_links)
        theta = np.deg2rad(np.random.normal(loc=mean_theta, scale=std_theta, size=args.num_links))

        # Compute the position of each joint
        J_G = calculate_joints_position(a, theta)
        J_G_samples[:, i] = J_G[0:2,0]
        

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

