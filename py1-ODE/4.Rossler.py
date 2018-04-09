#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:47:10 2018

@author: xwen
"""

import pkuode
import numpy as np

class ROSSLER(pkuode.ODE):
    def tend(self, state):
        x,y,z = state
        xt = -y-z
        yt = x+self.par[0]*y                 # par[0]=a=0.2
        zt = self.par[1]+z*(x-self.par[2])   # par[1]=b=0.2, par[2]=c=5.7
        tendency = np.array([xt,yt,zt])
        return tendency

if __name__ == "__main__":
    a = ROSSLER(ic=[1,1,1],dt=0.01,steps=90000,par=[0.2,0.2,5.7])
    a.Integrate()
    pkuode.plot3d(a.line,ti='Rossler Model',style='r-',lw=0.5)

