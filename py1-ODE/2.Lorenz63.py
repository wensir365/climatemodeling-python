#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:47:10 2018

@author: xwen
"""

import pkuode
import numpy as np

class L63(pkuode.ODE):
    def tend(self, state):
        x,y,z = state
        xt = self.par[0]*(y-x)              # par[0] = sigma = 10
        yt = x*(self.par[1]-z)-y            # par[1] = r = 28
        zt = x*y-self.par[2]*z              # par[2] = b = 8/3
        tendency = np.array([xt,yt,zt])
        return tendency

if __name__ == "__main__":
    a = L63(ic=[0.1,0.1,0.1],dt=0.01,steps=6000,par=[10,28,8/3])
    a.Integrate()
    pkuode.plot3d(a.line,ti='Lorenz63 Model',style='r-',lw=0.5)

    b = L63(ic=[-0.1,-0.1,-0.1],dt=0.01,steps=6000,par=[10,28,8/3])
    b.Integrate()
    pkuode.plot3d(b.line,ti='Lorenz63 Model',style='b-',lw=0.5)

    pkuode.plot3dcomp2(a.line,b.line,lb1="IC=[0.1,0.1,0.1]",lb2="IC=[-0.1,-0.1,-0.1]",ti="Lorenz63",lw=0.5)

    pkuode.plot2d(np.array([a.line[:3000,0],b.line[:3000,0]]).T,ti='Results from IC disturbance',xl='[0.1]',yl='[-0.1]')


