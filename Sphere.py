#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:52:59 2018

@author: user1
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

q = 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u, v = np.mgrid[0:2*np.pi:7j, 0:np.pi:7j]

Data = []

def Sphere(x0,y0,z0,r):
    x = x0+r*np.cos(u)*np.sin(v)
    y = y0+r*np.sin(u)*np.sin(v)
    z = z0+r*np.cos(v)
    Data.append(((x,y,z)))
    return np.array([x,y,z])

def Voltage(q,xg,yg,zg,vec):
    R = ((xg-vec[0])**2 + (yg-vec[1])**2 + (zg-vec[2])**2)**(1/2)
    return q*(xg - vec[0])/R , q*(yg - vec[1])/R , q*(zg - vec[2])/R

x0 = 0
y0 = 0
z0 = 0
r = 2

X = np.linspace(x0-5, x0+5, 7)
Y = np.linspace(y0-5, y0+5, 7)
Z = np.linspace(z0-5, z0+5, 7)
XX,YY,ZZ = np.meshgrid(X,Y,Z)

x,y,z = Sphere(x0,y0,z0,r)

Ex = np.zeros((7, 7, 7))
Ey = np.zeros((7, 7, 7))
Ez = np.zeros((7, 7, 7))

for Data in Data:
    ex, ey, ez = Voltage(q,XX,YY,ZZ,Data)
    Ex += ex
    Ey += ey
    Ez += ez

ax.quiver(XX, YY, ZZ, Ex, Ey, Ez, color = 'blue')
ax.plot_wireframe(x,y,z, color = 'black')
ax.scatter(x,y,z,s = 1, color = 'red')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_aspect('equal')
plt.savefig('sphere.png', dpi = 200)