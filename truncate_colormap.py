#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:00:59 2018

@author: jlee
"""


# Reference : https://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib


import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

def truncate_colormap(cmap, minval=0.0, maxval=1.0, nn=256):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({0},{1:.2f},{2:.2f})'.format(cmap.name, minval, maxval),
        cmap(np.linspace(minval, maxval, nn)))
    return new_cmap
