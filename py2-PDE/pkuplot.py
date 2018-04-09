#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:12:09 2018
@author: xwen@pku.edu.cn
"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

def quickview_array(z):
    '''
    原则上可以快速查看任何1D或2D的数组
    只要输入量z是numpy数组类型即可
    此子程序是对xarray.DataArray对象的封装而已
    Thanks to xarray package!!!
    '''
    z_array = xr.DataArray(z)
    plot = z_array.plot()
    return plot

def plot2d(N,x,y,style,lw,lb,
           ti="Plot",xl="X",yl="Y",legendloc=4,
           xlim=[],ylim=[],ylog=False,
           figsize=(10,6),
           fn="plot2d.pdf"):
    '''
    在x-y图上画N条线的函数
    ----------------------
    N          : 几条线？           N=2
    x,y        : 几条线对应的x和y   x=[time,time],y=[z700,z500]
    style      : 每条线的线型       style=['r-o','b-s']
    lw         : 每条线的线宽       lw=[2,4]
    lb         : 每条线的标识       lb=['Geopotential at 700mb', 'Geopotential at 500mb']
    ti         : 整张图的名称       ti='Comparison b/w Z500 and Z700'
    xl,yl      : x轴、y轴的label    xl='Longitude',yl='Geopotential Height (m)'
    legendloc  : legend位置         legendloc=0(auto),1,2,3,4,...,10
    xlim, ylim : x轴、y轴的范围     xlim=[0,360] （ylim可不给，代表由系统自主确定）
    ylog       : y轴是否logarithmic ylog=True
    figsize    : 图片尺寸           figsize=(10,6) for 10-inch width and 6-inch height
    fn         : 另存为PDF文件的文件名
    '''

    plt.figure(figsize=(12,8))

    for i in range(N):
      plt.plot(x[i],y[i],style[i],linewidth=lw[i],label=lb[i])

    plt.title(ti)
    plt.xlabel(xl)
    plt.ylabel(yl)

    if xlim: plt.xlim(xlim[0],xlim[1])
    if ylim: plt.ylim(ylim[0],ylim[1])
    if ylog: plt.yscale('log')

    plt.legend(shadow=True,loc=legendloc)

    plt.savefig(fn)
    plt.show()
    plt.close()

# Main
if __name__=='__main__':
   print("Main")

