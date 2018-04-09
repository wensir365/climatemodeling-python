#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:47:10 2018

@author: xwen
"""

import pkuode
import numpy as np

class RF(pkuode.ODE):
    def tend(self, state):
        x,y,z = state
        xt = y*(z-1+x*x)+self.par[0]*x          # par[0] = a = 0.87
        yt = x*(3*z+1-x*x)+self.par[0]*y
        zt = -2*z*(self.par[1]+x*y)             # par[1] = b = 1.1
        tendency = np.array([xt,yt,zt])
        return tendency

if __name__ == "__main__":
    a = RF(ic=[20,20,20],dt=0.0001,steps=20000,par=[0.87,1.1])
    a.Integrate()
    pkuode.plot3d(a.line,ti='Rabinovich-Fabrikant Model',style='r-',lw=0.5)

