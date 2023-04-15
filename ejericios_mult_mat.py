import numpy as np

theta = np.deg2rad(30)
a = 0.04

TL_1 = np.array([[np.cos(theta), -np.sin(theta), a*np.cos(theta)],[np.sin(theta), np.cos(theta), a*np.sin(theta)],[0,0,1]])

T1_2 = np.array([[np.cos(theta), -np.sin(theta), a*np.cos(theta)],[np.sin(theta), np.cos(theta), a*np.sin(theta)],[0,0,1]])

theta3 = np.deg2rad(-55)

P2 = np.array([a*np.cos(theta3), a*np.sin(theta3), 1])

#P1_2 = np.matmul(P2,T1_2)
PL_2 = np.matmul(np.matmul(TL_1,T1_2),P2)

print('******'*8)
print(PL_2)