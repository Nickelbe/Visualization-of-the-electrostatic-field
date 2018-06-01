#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:58:42 2018

@author: user1
"""
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

q = -5
eps0 = 8.8 * 10**(-12)
k = 1/4/3.14/eps0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def Potential(q,x,y,z,xq,yq,zq):
    R = ((x-xq)**2 + (y-yq)**2 + (z-zq)**2)**(1/2)
    return q*(x-xq)/(R**3), q*(y-yq)/(R**3), q*(z-zq)/(R**3)

a = 0
b = 0
c = 3
d = -0

xs = 6
ys = 6

x = np.arange((xs))
y = np.arange((ys))
              
X,Y = np.meshgrid(x, y)
Z = (-a*X - b*Y - d)/c
              
coor = (-a*xs - b*ys - d)/c

XG = np.linspace(xs/2 - 5, xs/2 + 5, 11)
YG = np.linspace(ys/2 - 5, ys/2 + 5, 11)
ZG = np.linspace(coor-5, coor+10, 11)
XX, YY, ZZ = np.meshgrid(XG, YG, ZG)

qs = q/(xs*ys)
xq = []
yq = []
zq = []

Ex = np.zeros((11,11,11))
Ey = np.zeros((11,11,11))
Ez = np.zeros((11,11,11))
              
for i in range(xs):
     for j in range(ys):
        xq.append(i)
        yq.append(j)
        zq.append((-a*i - b*j - d)/c)

for k in range(xs*ys):
    ex, ey, ez = Potential(qs,XX,YY,ZZ,xq[k],yq[k],zq[k])
    Ex += ex
    Ey += ey
    Ez += ez

ax.scatter(xq,yq,zq,color  = 'red')
ax.quiver(XX, YY, ZZ, Ex, Ey, Ez, color = 'blue')
#ax.plot_surface(X ,Y ,Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
fig.savefig('test2png.png', dpi=200)