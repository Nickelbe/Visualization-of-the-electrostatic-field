#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 00:06:21 2018

@author: user1
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(dpi = 200)
ax = fig.add_subplot(121, projection='3d')

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

#Greeting======================================================================

print('----------------------------------------------------------------------\n Программа для визуализации электрического поля\n Брагин Николай 10 фм класс, МХЛ 1303\n----------------------------------------------------------------------\n')

#==============================================================================

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

u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
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
    return k*q*(x-xq)/(R**3), k*q*(y-yq)/(R**3), k*q*(z-zq)/(R**3)

#simple charges' coordinates===================================================

print('Чтобы добавить точечные заряды выберите [Да/Нет]')

controller_0 = str(input())

if controller_0 == 'Да':
    print('Сначала введите число зарядов, затем их координаты (x,y,z) и заряд')
    n = int(input())
    for l in range(n):
        q0 = float(input())
        q.append(q0)
        x = int(input())
        xq.append(x)
        y = int(input())
        yq.append(y)
        z = int(input())
        zq.append(z)

#input of data for sphere======================================================

print('Чтобы добавить сферу выберите [Да/Нет]')

controller_1 = str(input())

if controller_1 == 'Да':
    print('Введите заряд сферы и ее радиус')
    sphere_q = float(input())
    sphere_x = 0
    sphere_y = 0
    sphere_z = 0
    sphere_r = int(input())

    x1,y1,z1 = Sphere(sphere_x, sphere_y, sphere_z, sphere_r, sphere_q)

#Input of data our surface plot need===========================================

print('Чтобы добавить плоскость выберите [Да/Нет]')

controller_2 = str(input())

if controller_2 == 'Да':
    print('Введите заряд плоскости, ее местоположение и коэффициенты (ax + by + cz + d)')
    q_su = float(input())
    x_coor = int(input())
    y_coor = int(input())
    xs_s = 6
    ys_s = 6
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

xg = np.linspace(-30,30,10)
yg = np.linspace(-30,30,10)
zg = np.linspace(-30,30,10)
XG,YG,ZG = np.meshgrid(xg,yg,zg)

#===Calculating of voltage by superposition principle in each cell of grid=====

x_Voltage_vector = np.zeros((10,10,10))
y_Voltage_vector = np.zeros((10,10,10))
z_Voltage_vector = np.zeros((10,10,10))

x_length = y_length = z_length = len(xq_total)

for i in range(x_length):
    ex, ey, ez = Voltage(q_total[i],XG,YG,ZG,xq_total[i],yq_total[i],
                         zq_total[i])
    x_Voltage_vector += ex
    y_Voltage_vector += ey
    z_Voltage_vector += ez
    
#Painting of all charges due to their sign ====================================

print('Чтобы видеть "размазывание" заряда выберите [Да/Нет]')

controller_3 = str(input())

if controller_3 == 'Да':
    ch = 0 
    for h in q_total:
        if h < 0:
            ax.scatter(xq_total[ch], yq_total[ch], zq_total[ch], s = 2,
                      color = 'blue')
        else:
            
            ax.scatter(xq_total[ch], yq_total[ch], zq_total[ch], s = 2,
                      color = 'red')
        ch = ch+1
    
#The whole plot================================================================

if controller_1 == 'Да':
    ax.plot_wireframe(x1, y1, z1, color = 'black')
if controller_2 == 'Да':
    ax.plot_wireframe(xq_s, yq_s, zq_s, s = 3, color = 'black')
ax.quiver(XG, YG, ZG, x_Voltage_vector, y_Voltage_vector, z_Voltage_vector, color = 'blue')#, length = 5, normalize=True)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_aspect('equal')

print('Представить расчетный график? [Да/Нет]')

#Расчетный график==============================================================

controller_4 = str(input())
if controller_4 == 'Да':
    ax1 = fig.add_subplot(122, projection='3d')
    ax1.set_xlabel('X Label')
    ax1.set_ylabel('Y Label')
    ax1.set_zlabel('Z Label')
    ax1.set_aspect('equal')

    xg1 = np.linspace(-30,30,10)
    yg1 = np.linspace(-30,30,10)
    zg1 = np.linspace(-30,30,10)
    XG1, YG1, ZG1 = np.meshgrid(xg1,yg1,zg1)

    x_Voltage_vector_1 = np.zeros((10,10,10))
    y_Voltage_vector_1 = np.zeros((10,10,10))
    z_Voltage_vector_1 = np.zeros((10,10,10))

    
    if controller_2 == 'Да':
        q.append(q_su)
        z_coor = (-a_s*x_coor - b_s*y_coor - d_s)/c_s
        xq.append(x_coor)
        yq.append(y_coor)
        zq.append(z_coor)
    
    if controller_1 == 'Да':
        q.append(sphere_q)
        xq.append(sphere_x)
        yq.append(sphere_y)
        zq.append(sphere_z)

    schetchik = len(q)

    for i in range(schetchik):
        ex1, ey1, ez1 = Voltage(q[i], XG1, YG1, ZG1, xq[i], yq[i], zq[i])
        x_Voltage_vector_1 += ex1
        y_Voltage_vector_1 += ey1
        z_Voltage_vector_1 += ez1

    if controller_1 == 'Да':
        ax1.plot_wireframe(x1, y1, z1, color = 'black')
    if controller_2 == 'Да':
        ax1.plot_wireframe(xq_s, yq_s, zq_s, s = 3, color = 'black')
    ax1.quiver(XG1, YG1, ZG1, x_Voltage_vector_1 , y_Voltage_vector_1 , z_Voltage_vector_1 , color = 'blue')

    if controller_3 == 'Да':
        ch = 0 
        for h in q:
            if h < 0:
                ax1.scatter(xq[ch], yq[ch], zq[ch], s = 2,
                      color = 'blue')
            else:
            
                ax1.scatter(xq[ch], yq[ch], zq[ch], s = 2,
                      color = 'red')
                ch = ch+1

#===============================================================================

plt.title('Электрическое поле некоторых заряженных объектов')
plt.show()




