import numpy as np
from numpy import cos

theta = np.deg2rad(30)
a = 0.04

TL_1 = np.array([[np.cos(theta), -np.sin(theta), a*np.cos(theta)],[np.sin(theta), np.cos(theta), a*np.sin(theta)],[0,0,1]])

T1_2 = np.array([[np.cos(theta), -np.sin(theta), a*np.cos(theta)],[np.sin(theta), np.cos(theta), a*np.sin(theta)],[0,0,1]])

TL_2 = np.matmul(TL_1,T1_2)

print(TL_2)

theta2 = np.deg2rad(-55)


T2_3 = np.array([[np.cos(theta2), -np.sin(theta2), a*np.cos(theta2)],[np.sin(theta2), np.cos(theta2), a*np.sin(theta2)],[0,0,1]])

TL_3 = np.matmul(TL_2,T2_3)

print('------'*8)
print(TL_3)

theta3 = np.deg2rad(210)

T3_4 = np.array([[np.cos(theta3), -np.sin(theta3), a*np.cos(theta3)],[np.sin(theta3), np.cos(theta3), a*np.sin(theta3)],[0,0,1]])

TL_4 = np.matmul(TL_3,T3_4)

print('------'*8)
print(TL_4)

theta4 = np.deg2rad(205)

T4_5 = np.array([[np.cos(theta4), -np.sin(theta4), a*np.cos(theta4)],[np.sin(theta4), np.cos(theta4), a*np.sin(theta4)],[0,0,1]])

TL_5 = np.matmul(TL_4,T4_5)

print('------'*8)
print(TL_5)

P5 = np.array([0.01, 0.025, 1])

PL_5 = np.matmul(TL_5,P5)

print('******'*8)
print(TL_5)