# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:48:08 2018

@author: Hugo L. D. de S. Cavalcante
"""

from numpy import *
from numpy.linalg import eig
from matplotlib.pyplot import *


def det(A):
    """ Calcula o determinante de uma matriz 2x2 """
    return (A[0,0]*A[1,1]-A[1,0]*A[0,1])

#def eigvectors_2x2(A, L1, L2):
#    """ retorna os autovetores da matriz A, 2x2 """
#    v1 = zeros(2)
#    v2 = zeros(2)
#    # autovetor associado ao autovalor L1
#    if abs(A[0,1])> 1e-16:
#        v1[0] = 1.0
#        v1[1] = (L1 -A[0,0])/A[0,1]
#    elif abs(A[1,0])> 1e-16:
#        v1[0] = 1.0
#        v1[1] = (L1 -A[0,0])/A[0,1]
#    else:
#        v1[1] = 1.0
#    # autovetor associado ao autovalor L2
#    if abs(A[0,1])> 1e-16:
#        v2[0] = 1.0
#        v2[1] = (L2 -A[0,0])/A[0,1]
#    elif abs(A[0,0])> 1e-16:
#        v2[1] = L2/A[0,0]
#    return v1, v2


A = array([[0, 1], [-2, -3]])
#A = array([[0, 1], [-1, 0.01]])

tau = trace(A)
Delta = det(A)
if (tau**2 -4*Delta) < 0.0 :
    print("os lambdas são complexos")
    lambda1 = (tau + 1j*sqrt(4*Delta-tau**2))/2
    lambda2 = (tau - 1j*sqrt(4*Delta-tau**2))/2
else:
    lambda1 = (tau + sqrt(tau**2 -4*Delta))/2
    lambda2 = (tau - sqrt(tau**2 -4*Delta))/2


fig1 = figure(1)
if lambda1.real>0.0 or lambda2.real>0.0:
    ### o p.f. na origem é instável
    plot(0, 0, 'o', color='black', markerfacecolor='white')
else:
    ### o p.f. na origem é estável
    plot(0, 0, 'o', color='black')
ax1 = gca()

### If the lambdas are real we can draw the eigenvectors:
if isreal(lambda1):
    print("Os lambdas são reais. Desenhando autovetores.")
    #v1, v2 = eigvectors_2x2(A, lambda1, lambda2)
    lambda12, (v1, v2) = eig(A)
    lambda1, lambda2 = lambda12
    xlim(1.1 * amin(-fabs([v1[0], v2[0], 1])), 1.1 * amax(fabs([v1[0], v2[0], 1])))
    ylim(1.1 * amin(-fabs([v1[1], v2[1], 1])), 1.1 * amax(fabs([v1[1], v2[1], 1])))
    ### desenha setas associadas a v1
    if lambda1>0.0:
        #arrow(0, 0, v1[0], v1[1], head_width = 0.1) ## seta na direção de v1
        #arrow(0, 0, -v1[0], -v1[1], head_width = 0.1) ## seta na direção de -v1
        ax1.annotate("", xy = (v1[0],v1[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
        ax1.annotate("", xy=(-v1[0], -v1[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))

    else:
        #arrow(v1[0], v1[1], -v1[0], -v1[1], head_width = 0.5) ## seta na direção da origem, partindo de v1
        #arrow(-v1[0], -v1[1], v1[0], v1[1], head_width = 0.5) ## seta na direção da origem partindo de -v1
        ax1.annotate("", xy = (0,0), xytext=(v1[0],v1[1]), arrowprops=dict(arrowstyle="->"))
        ax1.annotate("", xy=(0, 0), xytext=(-v1[0], -v1[1]), arrowprops=dict(arrowstyle="->"))
    ### desenha setas associadas a v2
    if lambda2>0.0:
        #arrow(0, 0, v2[0], v2[1], head_width = 0.1) ## seta na direção de v2
        #arrow(0, 0, -v2[0], -v2[1], head_width = 0.1) ## seta na direção de -v2
        ax1.annotate("", xy = (v2[0],v2[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
        ax1.annotate("", xy=(-v2[0], -v2[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))

    else:
        #arrow(v2[0], v2[1], -v2[0], -v2[1], head_width = 0.1, head_starts_at_zero = True, length_includes_head = True) ## seta na direção da origem, partindo de v2
        #arrow(-v2[0], -v2[1], v2[0], v2[1], head_width = 0.1, head_starts_at_zero = True, length_includes_head = True) ## seta na direção da origem partindo de -v2
        ax1.annotate("", xy = (0, 0), xytext=(v2[0], v2[1]), arrowprops=dict(arrowstyle="->"))
        ax1.annotate("", xy=(0, 0), xytext=(-v2[0], -v2[1]), arrowprops=dict(arrowstyle="->"))


####
#### Falta desenhar algumas soluções que sejam ilustrativas do comportamento geral das soluções
####

show()
