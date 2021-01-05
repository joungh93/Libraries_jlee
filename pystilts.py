#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 5 11:41:24 2021

@author: jlee
"""


import pandas as pd
import os


def wcs_match1(ra1, dec1, ra2, dec2, dcr, working_path,
               stilts_path="/home/jlee/Downloads/",
               find_method="best", join_method="1and2"):
    
    """
    Match the sources with WCS positions from two tables
    :param ra1: RA in degrees from catalog1 (numpy.array)
    :param dec1: Dec in degrees from catalog1 (numpyu.array)
    :param ra2: RA in degrees from catalog2 (numpy.array)
    :param dec2: Dec in degrees from catalog2 (numpy.array)
    :param dcr: Tolerance separation in arcsec (float)
    :param working_path: Working path (string)
    :param stilts_path: The path where stilts.jar file is located ---> must be finished with '/'
    :param find_method: Keyword 'find' in stilts tskymatch2
    :param join_method: Keyword 'join' in stilts tskymatch2
    :return: 
    """

    current_dir = os.getcwd()
    os.chdir(working_path)

    if (stilts_path[-1] != "/"):
        raise ValueError("Revise your STILTS path with the last character of '/'")
    else:
        pass

    df1 = pd.DataFrame(data={'ra':ra1, 'dec':dec1})
    df1.to_csv("df1.csv")
    
    df2 = pd.DataFrame(data={'ra':ra2, 'dec':dec2})
    df2.to_csv("df2.csv")

    com = "java -jar "+stilts_path+"stilts.jar tskymatch2 "
    com += "in1=df1.csv ifmt1=csv in2=df2.csv ifmt2=csv "
    com += "ra1=ra dec1=dec ra2=ra dec2=dec "
    com += f"error={dcr:.3f} find="+find_method+" join="+join_method+" "
    com += "out=out.csv ofmt=csv omode=out"

    print("Starting STILTS ...")
    os.system(com)
    print("STILTS matching process is done")
    print("Output catalog is out.csv")

    df_out = pd.read_csv("out.csv")
    idx1 = df_out['col1_1'].values
    idx2 = df_out['col1_2'].values
    sepr = df_out['Separation'].values

    os.chdir(current_dir)

    return [idx1, idx2, sepr]

