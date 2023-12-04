#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:29:41 2018

@author: jlee
"""

import numpy as np


def linear(img, scale_min=0.0, scale_max=1.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)
    
    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0
    
    y = x
    
    return y


def log(img, scale_min=0.0, scale_max=1.0, a=1000.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)
    
    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0

    y = np.log10(a*x+1.0)/np.log10(a)
    
    return y


def power(img, scale_min=0.0, scale_max=1.0, a=1000.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)

    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0   

    y = (a**(x)-1.0)/a
    
    return y


def sqrt(img, scale_min=0.0, scale_max=1.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)

    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0  

    y = np.sqrt(x)    

    return y


def square(img, scale_min=0.0, scale_max=1.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)

    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0 

    y = x**(2.0)

    return y    


def asinh(img, scale_min=0.0, scale_max=1.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)

    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0
    
    y = np.arcsinh(10.0*x)/3.0
    
    return y


def sinh(img, scale_min=0.0, scale_max=1.0):
    x = img.astype(float)
    y = np.zeros((img.shape[0],img.shape[1]), dtype=float)

    scale_min = float(scale_min)
    scale_max = float(scale_max)
    
    lo = (img <= scale_min)
    bw = ((img > scale_min) & (img < scale_max))
    hi = (img >= scale_max)
    
    x[lo] = 0.0
    x[bw] = (img[bw]-scale_min)/(scale_max-scale_min)
    x[hi] = 1.0
    
    y = np.sinh(3.0*x)/10.0    
    
    return y
    
