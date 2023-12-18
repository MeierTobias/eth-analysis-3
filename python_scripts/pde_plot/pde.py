#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example on how to use the PDE and separated PDE module to plot a partial differential equation.
This script is provided without any guarantees on reliability or correctness. Feel free to use and improve.

@author: Juri Pfammatter
"""
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import numpy as np

class separated_PDE():
    
    def __init__(self, F, G, p, L, c, title, timeseries, N=100):
        self.F = F
        self.G = G
        self.L = L
        self.c = c
        self.title = title
        self.timeseries = timeseries
        self.N = N
        
        
    def init_plot(self):

        sns.set_theme()
        sns.set(rc={'figure.figsize':(10,10),'figure.dpi':600})
        sns.set(font_scale = 1.5, font="serif")


        ax = plt.figure().add_subplot(projection='3d')
        ax.view_init(elev=40, azim=-45, roll=0)
        ax.set_facecolor("white")
        ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
        
        ax.tick_params(axis = "both", color = "white")
        
        
       
        return ax
    
    def plot(self):
        axs = self.init_plot()
        
        y_len = self.L/self.c*2.5 # choose according to visual liking
        x = np.linspace(0, 1, self.N)
        y = np.linspace(0, y_len, self.N) # two periods
        X,Y = np.meshgrid(x, y)
        Z = self.F(X)*self.G(Y)
        
        # surface_plot
        axs.plot_surface(X,Y,Z, 
                         linewidth=0, 
                         rstride=1, cstride=1,
                         alpha=0.7, 
                         antialiased=True,
                         cmap=cm.bwr)
        
        # IC
        axs.plot(x, np.zeros(self.N), Z[0], "blue", label="IC")
        
        # BC
        axs.plot(np.zeros(self.N), y, Z[:,0], "magenta", label="BC")
        axs.plot(np.ones(self.N)*x[-1], y, Z[:,-1], "magenta")
        
        # G(t)
        axs.plot(np.ones(self.N)*(-.1), y, self.G(y), "indigo", label="G(t)")
        axs.plot(np.ones(self.N)*x[-1]/2, y, self.G(y), "indigo", linestyle = "-.", linewidth = 2)
        
        # F(x)
        timeseries = self.timeseries
        axs.plot(x, np.ones(self.N)*y_len, self.F(x)*self.G(y_len), "teal", linewidth = 2, label="F(x)")
        for t in timeseries:
            axs.plot(x, np.ones(self.N)*t, self.F(x)*self.G(t), "teal", linestyle="-.", linewidth = 2)
        
        
        axs.set(xlim=(0, 1), ylim=(0, y_len), zlim=(0, 1),
               xlabel='$x$', ylabel='$t$',
               title = self.title)
        
        
        
        plt.gca().legend(facecolor = 'white',loc = "best", fontsize = 15)



class Laplace():
    
    def __init__(self, u, L, M, title, lines, N=100):
        self.u = u
        self.L = L
        self.title = title
        self.timeseries = lines
        self.N = N
        self.y_len = M
        
        
    def init_plot(self):

        sns.set_theme()
        sns.set(rc={'figure.figsize':(10,10),'figure.dpi':600})
        sns.set(font_scale = 1.5, font="serif")

        ax = plt.figure().add_subplot(projection='3d')
        ax.view_init(elev=40, azim=-45, roll=0)
        ax.set_facecolor("white")
        ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
        
        ax.tick_params(axis = "both", color = "white")
       
        return ax
    
    def plot(self):
        axs = self.init_plot()
        
        y_len = self.y_len
        x = np.linspace(0, self.L, self.N)
        y = np.linspace(0, y_len, self.N) # two periods
        X,Y = np.meshgrid(x, y)
        Z = self.u(X,Y)
        
        # surface_plot
        axs.plot_surface(X,Y,Z, 
                         linewidth=0, 
                         rstride=1, cstride=1,
                         alpha=1, 
                         antialiased=True,
                         cmap=cm.bwr)
        # sinh
        axs.plot(np.ones(self.N)*(-.1), y, self.u(x[-1]/2,y), "indigo")
        axs.plot(np.ones(self.N)*x[-1]/2, y, self.u(x[-1]/2,y), "indigo", linestyle = "-.", linewidth = 2)
        
        
        # zero
        axs.plot(x, np.zeros(self.N), Z[0], "magenta", label="$\partial$R=0")
        axs.plot(np.zeros(self.N), y, Z[:,0], "magenta")
        axs.plot(np.ones(self.N)*x[-1], y, Z[:,-1], "magenta")
        
        # dirichlet
        timeseries = self.timeseries
        axs.plot(x, np.ones(self.N)*y_len, self.u(x,self.timeseries[-1]), "teal", linewidth = 2, label="$\partial$R=f(x)")
        for t in timeseries[:-1]:
            axs.plot(x, np.ones(self.N)*t, self.u(x,t), "teal", linestyle="-.", linewidth = 2)
    
        axs.set(xlim=(0, self.L), ylim=(0, y_len),
               xlabel='$x$', ylabel='$y$',
               title = self.title)
        
        
        
        plt.gca().legend(facecolor = 'white',loc = "best", fontsize = 15)
        
        
class PDE():
    
    def __init__(self, u,L,title, timeseries, N=100, t_len = 2.5):
        self.u = u
        self.L = L
        self.title = title
        self.timeseries = timeseries
        self.N = N
        self.y_len = t_len
        
        
    def init_plot(self):

        sns.set_theme()
        sns.set(rc={'figure.figsize':(10,10),'figure.dpi':600})
        sns.set(font_scale = 1.5, font="serif")

        ax = plt.figure().add_subplot(projection='3d')
        ax.view_init(elev=40, azim=-45, roll=0)
        ax.set_facecolor("white")
        ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
        
        ax.tick_params(axis = "both", color = "white")
       
        return ax
    
    def plot(self):
        axs = self.init_plot()
        
        y_len = self.y_len
        x = np.linspace(0, self.L, self.N)
        y = np.linspace(0, y_len, self.N) # two periods
        X,Y = np.meshgrid(x, y)
        Z = self.u(X,Y)
        
        # surface_plot
        # Laplace Equation
        
        axs.plot_surface(X,Y,Z, 
                         linewidth=0, 
                         rstride=1, cstride=1,
                         alpha=0.7, 
                         antialiased=True,
                         cmap=cm.bwr)
            
        # IC
        axs.plot(x, np.zeros(self.N), Z[0], "blue", label="IC")
        
        # BC
        axs.plot(np.zeros(self.N), y, Z[:,0], "magenta", label="BC")
        axs.plot(np.ones(self.N)*x[-1], y, Z[:,-1], "magenta")
        
        # G(t)
        
        x_0 = Z[0].argmax()/(self.L*self.N)
        axs.plot(np.ones(self.N)*(-.1), y, self.u(x_0,y), "indigo", label="u($x_0$,t)")
        axs.plot(np.ones(self.N)*x_0, y, self.u(x_0,y), "indigo", linestyle = "-.", linewidth = 2)
        
        # F(x)
        timeseries = self.timeseries 
        axs.plot(x, np.ones(self.N)*y_len, self.u(x,self.timeseries[-1]), "teal", linewidth = 2, label="u(x,$t_0$)")
        for t in timeseries[:-1]:
            axs.plot(x, np.ones(self.N)*t, self.u(x,t), "teal", linestyle="-.", linewidth = 2)
            
        axs.set(xlim=(0, self.L), ylim=(0, y_len),
               xlabel='$x$', ylabel='$t$',
               title = self.title)
        
        
        plt.gca().legend(facecolor = 'white',loc = "best", fontsize = 15)