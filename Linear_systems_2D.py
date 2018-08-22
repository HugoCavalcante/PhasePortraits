# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:48:08 2018

@author: Hugo L. D. de S. Cavalcante
"""

from numpy import *
from matplotlib.pyplot import *


def det(A):
    """ Calcula o determinante de uma matriz 2x2"""
    return (A[0,0]*A[1,1]-A[1,0]*A[0,1])

#A = array([[0, 1], [-2, -3]])
A = array([[0, 1], [-1, 0.01]])

tau = trace(A)
Delta = det(A)
if (tau**2 -4*Delta) < 0.0 :
    print("os lambdas são complexos")
    lambda1 = (tau + 1j*sqrt(4*Delta-tau**2))/2
    lambda2 = (tau - 1j*sqrt(4*Delta-tau**2))/2
else:
    lambda1 = (tau + sqrt(tau**2 -4*Delta))/2
    lambda2 = (tau - sqrt(tau**2 -4*Delta))/2


