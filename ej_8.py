import numpy as np

theta = -60
a=4
R1 = np.array([[np.cos(theta),-np.sin(theta),-a*np.cos(theta)],[np.sin(theta), np.cos(theta),-a*np.sin(theta)],[0,0,1]])

theta2= 40
R2 = np.array([[np.cos(theta2),-np.sin(theta2),a*np.cos(theta2)],[np.sin(theta2), np.cos(theta2),a*np.sin(theta2)],[0,0,1]])

x = np.array([[0],[0],[1]])

TR = np.matmul(R1,x)
#print(TR)

TF = np.matmul(R2,TR)
#print(TF)

x2 = np.array([[-4],[0],[1]])
TR2 = np.matmul(R1,x2)
print(TR2)

