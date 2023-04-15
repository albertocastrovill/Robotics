import numpy as np

theta = np.deg2rad(45)

Rz = np.array([[np.cos(theta),-np.sin(theta),0,5],[np.sin(theta), np.cos(theta),0,5],[0,0,1,5],[0,0,0,1]])


P = np.array([-3,1,-2,1])

PG = np.matmul(Rz,P)

print(PG)