import numpy as np
import argparse
import matplotlib.pyplot as plt

# Parse
parser = argparse.ArgumentParser()

parser.add_argument('--a', type=float, nargs='+', help=" 2 Longitudes")
parser.add_argument('--theta', type=int, nargs='+', help=" 2 Angulos")

args = parser.parse_args()

#tx1 = args.a[1]*np.cos(np.deg2rad(args.theta[1]))
#ty1 = args.a[1]*np.sin(np.deg2rad(args.theta[1]))
#T1_2 = [[np.cos(np.deg2rad(args.theta[0])), -np.sin(np.deg2rad(args.theta[0])), tx],[np.sin(np.deg2rad(args.theta[0])), np.cos(np.deg2rad(args.theta[0])), ty],[0,0,1]]

#Rotate Matriz Function
def compute_rotation_matrix(theta):

    R = np.array([[np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta))],[np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta))]])

    return R

#Translation Matriz Function
def compute_translation(a,theta):
    tx = a*np.cos(np.deg2rad(theta))
    ty = a*np.sin(np.deg2rad(theta))
    t = np.array([tx,ty,1])
    return t

# Not finished function
def get_transformation_matrix(R, t):
    temp1 = np.hstack((R,t))
    temp2 = np.array([0,0,1])
    T = np.hstack()

    return T

# 
def compute_transformation_matrix(a,theta):
    R = compute_rotation_matrix(theta)
    print(R)
    t = compute_translation(a,theta)
    print(t)

    return get_transformation_matrix(R,t)

a3 = args.a[2]
a2 = args.a[1]
a1 = args.a[0]
theta3 = args.theta[2]
theta2 = args.theta[1]
theta1 = args.theta[0]

T2_1 = compute_transformation_matrix(a2,theta2)
TG_1 = compute_transformation_matrix(a1,theta1)
PG_2 = [a3*np.cos(np.deg2rad(theta3)), a3*np.sin(np.deg2rad(theta3)),1]
