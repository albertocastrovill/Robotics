import time
from zmqRemoteApi import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.getObject('sim')

base_id = sim.getObject('/Base')
joint1 = sim.getObject('/Base/Joint1')
joint2 = sim.getObject('/Base/Joint2')
link1 = sim.getObject('/Base/Link1')
link2 = sim.getObject('/Base/Link2')
dummy = sim.getObject('/Base/Dummy')

print(f'base: {base_id}')
print(f'joint1: {joint1}')
print(f'joint1: {joint2}')
print(f'joint1: {link1}')
print(f'joint1: {link2}')
print(f'joint1: {dummy}')

#client.setStepping(True)
sim.startSimulation()

#Rotate joint 1
theta = np.deg2rad(45)
sim.setJointTargetPosition(joint1,theta)

sim.stopSimulation()