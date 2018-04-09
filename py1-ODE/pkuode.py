#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:12:09 2018
@author: xwen@pku.edu.cn
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ODE:
   '''
   Class of ODE solver
   X. Wen, Peking Univ, Mar 2018
   
   ODE方程组求解器
   闻新宇，北京大学，2018年3月   
   '''
   
   def __init__(self,ic=[],dt=0.01,steps=1000,par=[],out=True):
      '''
      ic     : Initial Condition in a list
      dt     : Time step (sec)
      steps  : Number of total steps integrated
      par    : Optional parameters in a list
      out    : Want to print init info? True as default
      '''
      
      self.DIM = len(ic)
      self.dt, self.steps = dt, steps
      self.par = par
      self.line = np.ndarray(shape=(self.steps,self.DIM),dtype=float)
      self.line[0,:] = np.array(ic,dtype=float)
      
      if out: print("Initial condition of this ODE object =",ic)
      
   def tend(self,state):
      '''
      千万别忘了构造tend方法，来表达你的ODE方程组！
      '''
      
      # 3D Example
      #x,y,z = state
      #xt = self.par[0]*(y-x)
      #yt = x*(self.par[1]-z)-y
      #zt = x*y-self.par[2]*z
      #tendency = np.array([xt,yt,zt])
      
      # 2D Example
      #x,y = state
      #xt = self.par[0]*(x-y)
      #yt = self.par[1]*y-x**2
      #tendency = np.array([xt,yt])

      #return tendency
      pass

   def rk4(self,state):
      '''
      Runge-Kutta 4th order
      '''
      
      q1 = self.dt*self.tend(state)
      q2 = self.dt*self.tend(state+q1/2)
      q3 = self.dt*self.tend(state+q2/2)
      q4 = self.dt*self.tend(state+q3)
      statenew = state+(q1+2*q2+2*q3+q4)/6
      return statenew

   def Integrate(self):
      i = 1
      while i<self.steps:
         self.line[i,:] = self.rk4(self.line[i-1,:])
         i = i+1

   def Print(self):
      for i in range(self.steps):
          print(i,"...",self.line[i,:])


def plot2d(data,style="r-",lw=1.0,ti="Plot",xl="X",yl="Y",xlim=[],ylim=[],fn="plot2d.pdf"):
    x,y = data[:,0],data[:,1]
    plt.plot(x,y,style,linewidth=lw)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(ti)
    if xlim: plt.xlim(xlim[0],xlim[1])
    if ylim: plt.ylim(ylim[0],ylim[1])
    plt.savefig(fn)
    plt.show()
    plt.close()


def plot3d(data,style="r-",lw=1.0,ti="Plot",xl="X",yl="Y",zl="Z",fn="plot3d.pdf"):
    x,y,z = data[:,0],data[:,1],data[:,2]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set(title=ti,xlabel=xl,ylabel=yl,zlabel=zl)
    ax.plot(x,y,z,style,linewidth=lw)
    plt.savefig(fn)
    plt.show()
    plt.close()


def plot3dcomp2(data1,data2,lb1='L1',lb2='L2',lw=1.0,ti="Plot",xl="X",yl="Y",zl="Z",fn="plot3d.pdf"):
    x1,y1,z1 = data1[:,0],data1[:,1],data1[:,2]
    x2,y2,z2 = data2[:,0],data2[:,1],data2[:,2]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set(title=ti,xlabel=xl,ylabel=yl,zlabel=zl)
    ax.plot(x1,y1,z1,'r-',linewidth=lw,label=lb1)
    ax.plot(x2,y2,z2,'b-',linewidth=lw,label=lb2)
    plt.legend()
    plt.savefig(fn)
    plt.show()
    plt.close()


# Main
if __name__=='__main__':
   a = ODE(ic=[1,1])

