import numpy as np
import matplotlib.pyplot as plt
import argparse

# Parse
parser = argparse.ArgumentParser()

parser.add_argument('--a', type=float, nargs='+', help=" 2 Longitudes")
parser.add_argument('--theta', type=int, nargs='+', help=" 2 Angulos")

args = parser.parse_args()

a1 = args.a[1]

#x1 = args.a[0]*np.cos(np.deg2rad(args.theta[0]))
#y1 = args.a[0]*np.sin(np.deg2rad(args.theta[0]))

#x2 = args.a[1]*np.cos(np.deg2rad(args.theta[0]+args.theta[1]))
#y2 = args.a[1]*np.sin(np.deg2rad(args.theta[0]+args.theta[1]))

#tx = x1 + x2
#ty = y1 + y2

tx1 = args.a[1]*np.cos(np.deg2rad(args.theta[1]))
ty1 = args.a[1]*np.sin(np.deg2rad(args.theta[1]))


T = np.array([[np.cos(np.deg2rad(args.theta[0])), -np.sin(np.deg2rad(args.theta[0])), tx1],[np.sin(np.deg2rad(args.theta[0])), np.cos(np.deg2rad(args.theta[0])), ty1],[0,0,1]])
P1 = np.array([args.a[1]*np.cos(np.deg2rad(args.theta[0])), args.a[1]*np.sin(np.deg2rad(args.theta[0])), 1])
PG = np.matmul(T,P1)


print(f"P(x_G, y_G) = [{PG[0]}, {PG[1]}]")
