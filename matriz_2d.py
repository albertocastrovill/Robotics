import numpy as np
"""
theta = np.deg2rad(30)

R = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])
#print(R)

P = np.array([4,5,1])

PG = np.matmul(R,P)

print(PG)
"""

"""
#Ejercicio 12
def transf_matrix(theta, a):
    R = np.array([[np.cos(theta),-np.sin(theta),a*np.cos(theta)],[np.sin(theta), np.cos(theta),a*np.sin(theta)],[0,0,1]])
    return R

thetar = np.deg2rad(18.5)
theta4 = np.deg2rad(25)
theta3 = np.deg2rad(-75)
theta2 = np.deg2rad(-40)
theta1 = np.deg2rad(60)

x = np.array([[2.5*np.cos(thetar)],[2.5*np.sin(thetar)],[1]])
#print(x)

x = np.matmul(transf_matrix(theta4,0.5),x)
print("-----"*10)
print(x)
x = np.matmul(transf_matrix(theta3,4),x)
print("-----"*10)
print(x)
x = np.matmul(transf_matrix(theta2,4),x)
print("-----"*10)
print(x)
x = np.matmul(transf_matrix(theta1,4),x)
print("-----"*10)
print(x)


theta = np.deg2rad(180)
R = np.array([[np.cos(theta),-np.sin(theta),16.2],[np.sin(theta), np.cos(theta),7.75],[0,0,1]])
x = np.matmul(R,x)
print(x)
"""
#Ejercicio 11

#x_1 = 4*np.cos(60)
#y_1 = 4*np.sin(60)
#print(x_1 , y_1)

def transf_matrix(theta, a):
    R = np.array([[np.cos(theta),-np.sin(theta),-a*np.cos(theta)],[np.sin(theta), np.cos(theta),-a*np.sin(theta)],[0,0,1]])
    return R

x = np.array([[0],[0],[1]])

"""
T1_L = np.matmul(transf_matrix(-30,4),x)
print(T1_L)
print("-----"*10)
TG_L = np.matmul(transf_matrix(60,4),T1_L)
print(TG_L)
"""

T1 = transf_matrix(60,4)
T2 = transf_matrix(-40,4)

#T1_2 = np.matmul(T1,T2)
T1_3 = np.matmul(T2,x)
TF = np.matmul(T1,T1_3)
print(T1_3)
print("-----"*10)
print(TF)


