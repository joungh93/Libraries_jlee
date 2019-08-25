#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:12:13 2019

@author: jlee
"""

import numpy as np

def func_ell(x, y, a, b, theta_deg, x0=0.0, y0=0.0):
    theta_rad = theta_deg*(np.pi/180.)
    cxx = (np.cos(theta_rad)/a)**2.0 + (np.sin(theta_rad)/b)**2.0
    cyy = (np.sin(theta_rad)/a)**2.0 + (np.cos(theta_rad)/b)**2.0
    cxy = 2.0*np.cos(theta_rad)*np.sin(theta_rad)*(1./a**2.0 - 1./b**2.0)
    
    val = cxx*(x-x0)**2.0 + cyy*(y-y0)**2.0 + cxy*(x-x0)*(y-y0) - 1.0
    return val