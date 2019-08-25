#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:05:23 2018

@author: jlee
"""

import numpy as np
from cctr import *

# Virial mass with NFW profile
#rec = np.arange(1000)/50.
#m10 = np.array([1.0e+0, 1.0e+1, 1.0e+2, 1.0e+3])
#G=6.674d-8  # CGS [cm^3 g^(-1) s^(-2)]
G = 4.302e-9  # [(km/s)^2 Mpc M_Sun^(-1)]
h100 = 67.8  # Hubble constant [km/s/Mpc]
h = h100 / 100.0
pc = 3.086e+18  # 1pc to cm

def m_encl(R_h, m10):
    # R_h : 3-D half-light radii
    # m10 : m10*1.0e+10 solar mass
    
    m200 = m10*1.0e+10  # solar mass
    c = cctr(m10,0.0)
    R200 = 1000.0*((G*m200)/(100.0*h100*h100))**(1./3)
    
    v1 = m200/(np.log(1.0+c)-c/(1.0+c))
    v2 = np.log(1.0+c*R_h/R200) - (c*R_h/R200)/(1.0+c*R_h/R200)

    return v1*v2