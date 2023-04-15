import numpy as np
import matplotlib.pyplot as plt
import argparse

# Parse user's arguments from command line
parser = argparse.ArgumentParser()

parser.add_argument('-initial', type=int, default=0, help="Initial Angle in degrees")
parser.add_argument('-final', type=int, default=45, help="Final Angle in degrees")
parser.add_argument('-constant', type=int, default=0, help="Constant Rotation Angle between Initial and Final Angle in degrees")
args = parser.parse_args()

#Rotate Matriz Function
def create_R(theta):

    R = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

    return R


#Function that multiply the rotation matriz and coordinates
def apply_transform(R,x):

    x_p = np.matmul(R,x)

    return x_p


x0 = 0.30
y0 = 0
x = np.array([[x0] , [y0]])

#Variables
inicial=args.initial 
final = args.final
const = args.constant
j=0
i=0

for i in range (final+1): #Loop to calculate and plot every x and y point for every degree
    j+=1
    print(i)
    i = np.deg2rad(i) #Changing degrees to radians
    
    R0 = create_R(i) #Rotate Matriz Function
    #print(R0)
    
    x_p = apply_transform(R0,x) #Function that multiply the rotation matriz and coordinates
    print(x_p)
    if i == inicial:
        plt.scatter(x_p[0], x_p[1])

    elif j == const:
        print(j)
        plt.scatter(x_p[0], x_p[1])
        j = j-const
    
    elif i == final:
        plt.scatter(x_p[0], x_p[1])



plt.plot([0,0.3],[0,0], 'b-') #Ploting x line
plt.plot([0,0],[0,0.3], 'b-') #Ploting y line

plt.title(" Rotation of robotic arm")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()