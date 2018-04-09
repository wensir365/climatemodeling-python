#!/usr/bin/env python3

import numpy as np
import pkuplot
import pkupde

if __name__=='__main__':

   # Define x dimensions
   N  = 16
   xx = pkupde.generate_2pi(N)
   dd = xx[1]-xx[0]
   print(xx)

   # Original N
   NN = np.sin(xx)

   # pNpX : FD methods
   NN_ana   = np.cos(xx)
   NN_for1  = pkupde.for1_1d(NN,d=dd)
   NN_bak1  = pkupde.bak1_1d(NN,d=dd)
   NN_cen2  = pkupde.cen2_1d(NN,d=dd)
   NN_cen4  = pkupde.cen4_1d(NN,d=dd)

   pkuplot.plot2d(6,[xx,xx,xx,xx,xx,xx],[NN,NN_ana,NN_for1,NN_bak1,NN_cen2,NN_cen4],
      lb=['N (dim='+str(N)+')','pNpX Analytic','pNpX For1','pNpX Bak1','pNpX Cen2','pNpX Cen4'],
      style=['k--','y-','r-','b-','g-o','c-^'],
      lw=[2,6,2,2,2,2],
      xl='X',yl='N or pNpX',
      xlim=[0,np.pi*2],
      ti='Comparison of multiple FD methods')

   # Check differences
   DD_ana   = NN_ana - NN_ana
   DD_for1  = NN_for1 - NN_ana
   DD_bak1  = NN_bak1 - NN_ana
   DD_cen2  = NN_cen2 - NN_ana
   DD_cen4  = NN_cen4 - NN_ana

   pkuplot.plot2d(5,[xx,xx,xx,xx,xx],[DD_ana,DD_for1,DD_bak1,DD_cen2,DD_cen4],
                  lb=['Ideal no-bias','For1 - Analytic','Bak1 - Analytic','Cen2 - Analytic','Cen4 - Analytic'],
                  style=['k--','r-','b-','g-o','c-^'],
                  lw=[4,4,4,2,2],
                  xl='X',yl='N_finite - N_anal',
                  xlim=[0,np.pi*2],
                  ylim=[-0.4,0.4],
                  ti='Differences b/w N_finite and N_analytic', fn='plot2d-diff.pdf')

