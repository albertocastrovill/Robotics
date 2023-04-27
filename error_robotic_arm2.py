"""

Code Description:
EL codigo realiza cada una de las transformaciones de los eslabones de un brazo robótico y 
calcula el error de las posibles posiciones en las que se encotrará cada eslabón dependiendo 
de la desviación estandar de los argumentos (a , theta).
El usuario tiene la opción de escoger con cuantos eslabones trabajar, el numero de iteraciones, 
las distancias de cada eslabón y los ángulos de cada uno, así como las desviaciones estandar.


Example Code for Terminal:

python error_robotic_arm2.py --num_links 4 --iters 10 --a 40 40 40 40 --s_a 0.1 --theta 45 30 10 -20 --s_theta 0.25

"""

import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--num_links', type=int, default=1, help="Number of Links of the Robotic Arm")
parser.add_argument('--iters', type=int, default=100, help="Iterations")
parser.add_argument('--a', type=float, nargs='+', default=0.0, help="Mean A")
parser.add_argument('--s_a', type=float, default=0.1, help="Standard Deviation A")
parser.add_argument('--theta', type=int, nargs='+', default=0, help="Mean Theta")
parser.add_argument('--s_theta', type=float, default=0.25, help="Standard Deviation Theta")

args = parser.parse_args()


def variable_init():
    global mean_a, std_a, mean_theta, std_theta, NITERS, J_G_samples

    # Define uncertainties associated to joints and links
    mean_a, std_a = args.a, args.s_a
    mean_theta, std_theta = args.theta, args.s_theta

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
        a = np.random.normal(loc=mean_a[i], scale=std_a)
        theta = np.deg2rad(np.random.normal(loc=mean_theta[i], scale=std_theta))

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
        joint_positions = calculate_joint_positions(args.num_links, mean_a, std_a, mean_theta, std_theta)
        joint_positions = joint_positions.T

        # Save joint positions for plotting
        J_G_samples[:,i] = joint_positions.reshape(-1)


    # Compute mean of each error data points
    mean_J = np.mean(J_G_samples.reshape(args.num_links, 2, NITERS), axis=2)

    # Visualise the error propagation
    plt.figure(1, figsize=(10,10))

    plt.scatter(0, 0, s=20, color='b')
    
    for j in range(args.num_links):
        plt.scatter(J_G_samples[2*j,:], J_G_samples[2*j+1,:], s=5)
        plt.scatter(mean_J[j,0], mean_J[j,1], s=20, color='b')
        if j > 0 :
            plt.plot([mean_J[j-1,0], mean_J[j,0]], [mean_J[j-1,1], mean_J[j,1]], 'r', linewidth=2)
        else:
            plt.plot([0, mean_J[j,0]], [0, mean_J[j,1]], 'r',linewidth=2)
    
    plt.axis('equal')
    #plt.xlim([-mean_a[0], mean_a[0]*(args.num_links+1)])
    #plt.ylim([-mean_a[0], mean_a[0]*(args.num_links+1)])
    plt.show()
