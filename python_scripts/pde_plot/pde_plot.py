#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example on how to use the PDE and separated PDE module to plot a partial differential equation.
This script is provided without any guarantees on reliability or correctness. Feel free to use and improve.

@author: Juri Pfammatter
"""

import pde
import numpy as np
import matplotlib.pyplot as plt

#%%
""" Example of separated 1D-PDE """

title = "1D-Wave Equation"
L = 1
c = 6e-1
p = L/c
timeseries = [0.25*p, 0.5*p,1.75*p, 2*p, 2.25*p]

F = lambda x: np.sin(np.pi/L*x)
G = lambda t: L/(c*np.pi)*np.sin(c*np.pi/L*t)

pde1 = pde.separated_PDE(F, G, p, L, c, title, timeseries, N=200)
pde1.plot()
# plt.savefig('1d_wave.png', dpi = 200)

#%%
""" Example of 1D-PDE approximation by Fourier Series """

title = "1D-Wave Equation - Fourier Series"
L = 1
c = 1
p = L/c
k = 1
# lines to visualize f(t) at different times t
timeseries = [1*p, 1.25*p, 1.5*p, 1.75*p,2.5*p, 2*p] # the last sets the filled line

N = 300

def u(x,t):
    un = 0
    for n in range(1,N+1):
        un = un+ np.sin(n*np.pi/L*x)*(-1)**(n+1)/n**3*np.cos(n*np.pi/L*t)
    return un*12*k/np.pi**3
    
# F = lambda x: np.sin(np.pi/L*x)
# G = lambda t: L/(c*np.pi)*np.sin(c*np.pi/L*t)

pde1 = pde.PDE(u, p, L,title, timeseries, N=200)
pde1.plot()
# plt.savefig('1d_wave_fs.png', dpi = 200)

#%%
""" Example of 2D Laplace equation """

title = "2D-Laplace Equation"
L = 1
c = 5
p = L/c
k = 1
# lines to visualize f(x) at different values of y
lines = [1.2*p, 1.4*p, 1.6*p, 1.8*p, 2*p] # the last sets the filled line

N = 5

def u(x,t):
    un = 0
    for n in range(1,N+1):
        un = un+ np.sin(n*np.pi/L*x)*(-1)**(n+1)/n**3*np.sinh(n*np.pi/L*t)
    return un*12*k/np.pi**3

pde1 = pde.Laplace(u, p, L, 2*p, title, lines, N=200)
pde1.plot()
# plt.savefig('2d_laplace.png', dpi = 200)
