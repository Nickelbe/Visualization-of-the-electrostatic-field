#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:43:09 2018

@author: user1
"""
import matplotlib.pyplot as plt
import numpy as np

eps0 = 8.8 * 10**(-12)
k = 1/4/3.14/eps0

def Voltage(q,x,y,yq,xq):
    R = np.hypot(x-xq, y-yq)**3
    return q * (x - xq) / R, q * (y - yq) / R

q = []
xq = []
yq = []

x = np.linspace(-50,50,128)
y = np.linspace(-50,50,128)
X,Y = np.meshgrid(x,y)

n = int(input())

for i in range(n):
    a = int(input())
    q.append(a)
    b = int(input())
    xq.append(b)
    c = int(input())
    yq.append(c)

x_Voltage_vector = np.zeros((128, 128))
y_Voltage_vector = np.zeros((128, 128))

for j in range(n):
    ex, ey = Voltage(q[j],X,Y,yq[j],xq[j])
    x_Voltage_vector += ex
    y_Voltage_vector += ey
        
fig, ax1 = plt.subplots()

for k in range(n):
    if q[k] < 0:
        ax1.scatter(xq[k],yq[k], color = 'blue')
    else:
        ax1.scatter(xq[k],yq[k], color = 'red')

graduate = 2 * np.log(np.hypot(x_Voltage_vector, y_Voltage_vector))
ax1.streamplot(x, y, x_Voltage_vector, y_Voltage_vector, color= graduate, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
ax1.set_xlim(-50,50)
ax1.set_ylim(-50,50)
plt.title('Electric field visualization')
fig.savefig('2d.png', dpi = 500)
