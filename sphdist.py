#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:05:35 2018

@author: jlee
"""

import numpy as np

def sphdist(ra1, dec1, ra2, dec2):  # in degrees
    dra = np.abs(ra2-ra1)
    dtheta = np.arccos(np.sin(dec1*np.pi/180.)*np.sin(dec2*np.pi/180.) + \
                       np.cos(dec1*np.pi/180.)*np.cos(dec2*np.pi/180.)*np.cos(dra*np.pi/180.))
    
    return dtheta*(180./np.pi)