#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 00:06:21 2018

@author: user1
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

eps0 = 8.8 * 10**(-12)
k = 1/4/3.14/eps0

xq_s = []
yq_s = []
zq_s = []
q_s = []

xq2 = []
yq2 = []
zq2 = []
q2 = []

xq = []
yq = []
zq = []
q = []

#Creating Surface==============================================================

def Surface(q,x,y,xs,ys,a,b,c,d):
    q_surface = q/(xs*ys)
    zag_x = np.linspace(x - (xs/2), x + (xs/2), xs)
    zag_y = np.linspace(y - (ys/2), y + (ys/2), ys)
    X,Y = np.meshgrid(zag_x, zag_y)      
    for i in zag_x:
       for j in zag_y:
        xq_s.append(i)
        yq_s.append(j)
        zq_s.append((-a*i - b*j - d)/c)
        q_s.append(q_surface)

#Sphere========================================================================

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
def Sphere(x0,y0,z0,r,q):
    q_sphere = q/(20*20)
    x = x0+r*np.cos(u)*np.sin(v)
    y = y0+r*np.sin(u)*np.sin(v)
    z = z0+r*np.cos(v)
    xq2.append(x)
    yq2.append(y)
    zq2.append(z)
    q2.append(q_sphere)
    return np.array([x,y,z])

#This Function returns E vector separated to x.y.z axis =======================
    
def Voltage(q,x,y,z,xq,yq,zq):
    R = ((x-xq)**2 + (y-yq)**2 + (z-zq)**2)**(1/2)
    return q*(x-xq)/(R**3), q*(y-yq)/(R**3), q*(z-zq)/(R**3)

#simple charges' coordinates===================================================

n = int(input())
for l in range(n):
    q0 = int(input())
    q.append(q0)
    x = int(input())
    xq.append(x)
    y = int(input())
    yq.append(y)
    z = int(input())
    zq.append(z)

#input of data for sphere======================================================

sphere_q = int(input())
sphere_x = int(input())
sphere_y = int(input())
sphere_z = int(input())
sphere_r = int(input())

x1,y1,z1 = Sphere(sphere_x, sphere_y, sphere_z, sphere_r, sphere_q)

#Input of data our surface plot need===========================================

q_su = int(input())
x_coor = int(input())
y_coor = int(input())
xs_s = int(input())
ys_s = int(input()) 
a_s = int(input())
b_s = int(input())
c_s = int(input())
d_s = int(input())

Surface(q_su, x_coor, y_coor, xs_s, ys_s, a_s, b_s, c_s, d_s)

#Creating grid for our voltage arrows==========================================

xq_total = xq_s + xq2 + xq
yq_total = yq_s + yq2 + yq
zq_total = zq_s + zq2 + zq
q_total = q_s + q2 + q

xg = np.linspace(-20,20,20)
yg = np.linspace(-20,20,20)
zg = np.linspace(-20,20,20)
XG,YG,ZG = np.meshgrid(xg,yg,zg)

#===Calculating of voltage by superposition principle in each cell of grid=====

x_Voltage_vector = np.zeros((20,20,20))
y_Voltage_vector = np.zeros((20,20,20))
z_Voltage_vector = np.zeros((20,20,20))

x_length = y_length = z_length = len(xq_total)

for i in range(x_length):
    ex, ey, ez = Voltage(q_total[i],XG,YG,ZG,xq_total[i],yq_total[i],
                         zq_total[i])
    x_Voltage_vector += ex
    y_Voltage_vector += ey
    z_Voltage_vector += ez
    
#Painting of all charges due to their sign ====================================
ch = 0 
for h in q_total:
    if h < 0:
        ax.scatter(xq_total[ch], yq_total[ch], zq_total[ch], s = 2, 
                   color = 'violet')
    else:
        ax.scatter(xq_total[ch], yq_total[ch], zq_total[ch], s = 2,
                   color = 'red')
    ch = ch+1
    
#The whole plot================================================================

ax.plot_wireframe(x1, y1, z1, color = 'black')
ax.scatter(xq_s, yq_s, zq_s, s = 1, color = 'black')
ax.quiver(XG, YG, ZG, x_Voltage_vector, y_Voltage_vector, z_Voltage_vector,
          color = 'blue')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_aspect('equal')
plt.title('Electric field of charged sphere, points and surface')

ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
ax.set_zlim(-20,20)

fig.savefig('total.png', dpi = 1000)
































