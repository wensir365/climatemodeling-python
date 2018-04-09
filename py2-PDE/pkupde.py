#!/usr/bin/env python3

import numpy as np

def for1_1d(z,d=1):
   '''
   z  : the list of raw data, e.g. [1.2, 34, 23, 25]
   d  : dicrete grid space, default=1.0
   '''
   Ni = len(z)
   dzdi = np.array(range(Ni),dtype=float)
   for i in range(Ni):
      if i==(Ni-1):
          dzdi[i] = ( z[0] - z[i] ) / d
      else:
          dzdi[i] = ( z[i+1] - z[i] ) / d
   return dzdi


def bak1_1d(z,d=1):
   '''
   z  : the list of raw data, e.g. [1.2, 34, 23, 25]
   d  : dicrete grid space, default=1.0
   '''
   Ni = len(z)
   dzdi = np.array(range(Ni),dtype=float)
   for i in range(Ni):
      dzdi[i] = ( z[i] - z[i-1] ) / d
   return dzdi


def cen2_1d(z,d=1):
   '''
   z  : the list of raw data, e.g. [1.2, 34, 23, 25]
   d  : dicrete grid space, default=1.0
   '''
   Ni = len(z)
   dzdi = np.array(range(Ni),dtype=float)
   d2 = d*2
   for i in range(Ni):
      if i==(Ni-1):
          dzdi[i] = ( z[0] - z[i-1] ) / d2
      else:
          dzdi[i] = ( z[i+1] - z[i-1] ) / d2
   return dzdi


def cen4_1d(z,d=1):
   '''
   z  : the list of raw data, e.g. [1.2, 34, 23, 25]
   d  : dicrete grid space, default=1.0
   '''
   Ni = len(z)
   dzdi = np.array(range(Ni),dtype=float)
   d12 = d*12
   for i in range(Ni):
      if i==(Ni-1):
          dzdi[i] = ( -z[1] +8*z[0] -8*z[i-1] +z[i-2] ) / d12
      elif i==(Ni-2):
          dzdi[i] = ( -z[0] +8*z[i+1] -8*z[i-1] +z[i-2] ) / d12
      else:
          dzdi[i] = ( -z[i+2] +8*z[i+1] -8*z[i-1] +z[i-2] ) / d12
   return dzdi


def generate_2pi(N,opt=0):
   x  = np.linspace(start=0.0,stop=2*np.pi,num=N+1)
   xx = x[:-1]
   dd = xx[1]-xx[0]
   xx = xx+dd/2
   return xx


if __name__=='__main__':
   print("Main")

