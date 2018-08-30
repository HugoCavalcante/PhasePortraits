# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:00:56 2018

@author: Hugo L. D. de S. Cavalcante
"""

from numpy import *
#from numpy.linalg import eig
from matplotlib.pyplot import *

### numero de pontos na solução (tempo)
n = 5
dt = 0.05

def fx(x,y):
    return x*(3-x-2*y)

def fy(x,y):
    return y*(2-x-y)

def f(X):
    return array([fx(X[0],X[1]), fy(X[0],X[1])])

def solucao_PVI(x0, y0):
    X = zeros((n,2))
    X[0,:] = x0, y0
    for i in range(0,n-1):
        k1 = dt*f(X[i,:])
        k2 = dt*f(X[i,:]+0.5*k1)
        k3 = dt*f(X[i,:]+0.5*k2)
        k4 = dt*f(X[i,:]+k3)
        X[i+1,:] = X[i,:] + (k1+2*(k2+k3)+k4)/6
    return X

#dt = 0.05

xmin, xmax = 0.0, 3.5
ymin, ymax = 0.0, 2.5

N, M = 20, 20
Px = zeros((N,M))
Py = zeros((N,M))
Vx = zeros((N,M))
Vy = zeros((N,M))

for  j in range(M):
    Px[:,j] = linspace(xmin, xmax, N)
for  j in range(N):
    Py[j,:] = linspace(ymin, ymax, M)
for  j in range(M):
    Vx[:,j] = fx(Px[:,j], Py[:,j])
for  j in range(N):
    Vy[j,:] = fy(Px[j,:], Py[j,:])

figure()
#plot(Px, Py, '.')
xlim([xmin,xmax])
ylim([ymin,ymax])
xlabel('x')
ylabel('y')

#for i in range(N):
#    for j in range(M):
#        annotate("", xy = (dt*Vx[i,j]+Px[i,j],dt*Vy[i,j]+Py[i,j]), xytext=(Px[i,j],Py[i,j]), arrowprops=dict(arrowstyle="->"))

#for i in range(N):
#    for j in range(M):
#        X = solucao_PVI(Px[i,j], Py[i,j])
#        plot(X[:,0], X[:,1], c = 'black')
    
#quiver(Px[:,0],Py[0,:], Vx[:,:], Vy[:,:])
imshow(Vx)
imshow(Vy)
