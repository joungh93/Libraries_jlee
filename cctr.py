#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:41:44 2018

@author: jlee
"""

import numpy as np

# Virial mass with NFW profile
rec = np.arange(1000)/50.
m10 = np.array([1.0e+0, 1.0e+1, 1.0e+2, 1.0e+3])
m200 = m10*1.0e+10  # solar mass
#G=6.674d-8  # CGS [cm^3 g^(-1) s^(-2)]
G = 4.302e-9  # [(km/s)^2 Mpc M_Sun^(-1)]
h100 = 67.8  # Hubble constant [km/s/Mpc]
h = h100 / 100.0
pc = 3.086e+18  # 1pc to cm


def cctr(m10, z):
    # m10 = m10*1.0e+10 solar mass
    # z = redshift
    
    c0 = 3.395 * (1.0+z)**(-0.215)
    beta = 0.307 * (1.0+z)**(0.540)
    gamma1 = 0.628 * (1.0+z)**(-0.047)
    gamma2 = 0.317 * (1.0+z)**(-0.893)
    
    a = 1./(1.0+z)    
    Dz = 1.0
    
    nu0 = (4.135 - 0.564/a - 0.210/a**2 + 0.0557/a**3 - 0.00348/a**4) / Dz
    
    xi = (m10*h)**(-1.0)
    
    d1 = 22.26*xi**(0.292)
    d2 = 1.0 + 1.53*xi**(0.275) + 3.36*xi**(0.198)
    
    sigma = Dz * (d1 / d2)
    
    nu = 1.686 / sigma
    
    c = c0 * (nu/nu0)**(-gamma1) * (1.0+(nu/nu0)**(1./beta))**(-beta*(gamma2-gamma1))
    
    return c
    
    
    
    
    
    
    
    
    
    
    
    
    
    