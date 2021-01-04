#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:28:20 2019

@author: jlee
"""


import numpy as np
from astroquery.vizier import Vizier 
from astroquery.ned import Ned
import astropy.units as u 
import astropy.coordinates as coord


def gaia1_query(ra_deg, dec_deg, rad_deg, maxmag=20, 
               maxsources=10000): 
    """
    Query Gaia DR1 @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit G magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
#    vquery = Vizier(columns=['Source', 'RA_ICRS', 'DE_ICRS', 
#                             'phot_g_mean_mag', 'Plx'], 
#                    column_filters={"phot_g_mean_mag": 
#                                    ("<%f" % maxmag)}, 
#                    row_limit = maxsources) 
    vquery = Vizier(columns=['*'], 
                    column_filters={"phot_g_mean_mag": 
                                    ("<%f" % maxmag)}, 
                    row_limit = maxsources) 
 
    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg, 
                           unit=(u.deg, u.deg), 
                           frame='icrs')
    return vquery.query_region(field, 
                               width=("%fd" % rad_deg), 
                               catalog="I/337/gaia")[0] 


def gaia2_query(ra_deg, dec_deg, rad_deg, maxmag=20, 
               maxsources=10000): 
    """
    Query Gaia DR2 @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit G magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
#    vquery = Vizier(columns=['Source', 'RA_ICRS', 'DE_ICRS', 
#                             'phot_g_mean_mag', 'Plx'], 
#                    column_filters={"phot_g_mean_mag": 
#                                    ("<%f" % maxmag)}, 
#                    row_limit = maxsources) 
    vquery = Vizier(columns=['*'], 
                    column_filters={"phot_g_mean_mag": 
                                    ("<%f" % maxmag)}, 
                    row_limit = maxsources)     
 
    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg, 
                           unit=(u.deg, u.deg), 
                           frame='icrs')
    return vquery.query_region(field, 
                               radius=("%fd" % rad_deg), 
                               catalog="I/345/gaia2")[0] 


def gaia3_query(ra_deg, dec_deg, rad_deg, maxmag=20, 
               maxsources=10000): 
    """
    Query Gaia DR3 @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit G magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
#    vquery = Vizier(columns=['Source', 'RA_ICRS', 'DE_ICRS', 
#                             'phot_g_mean_mag', 'Plx'], 
#                    column_filters={"phot_g_mean_mag": 
#                                    ("<%f" % maxmag)}, 
#                    row_limit = maxsources) 
    vquery = Vizier(columns=['*'], 
                    column_filters={"phot_g_mean_mag": 
                                    ("<%f" % maxmag)}, 
                    row_limit = maxsources)     
 
    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg, 
                           unit=(u.deg, u.deg), 
                           frame='icrs')
    return vquery.query_region(field, 
                               radius=("%fd" % rad_deg), 
                               catalog="I/350/gaiaedr3")[0] 


def panstarrs_query(ra_deg, dec_deg, rad_deg, maxmag=20,
                    maxsources=10000):
    """
    Query PanSTARRS @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit R magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
#    vquery = Vizier(columns=['objID', 'RAJ2000', 'DEJ2000',
#                             'e_RAJ2000', 'e_DEJ2000',
#                             'gmag', 'e_gmag',
#                             'rmag', 'e_rmag',
#                             'imag', 'e_imag',
#                             'zmag', 'e_zmag',
#                             'ymag', 'e_ymag'],
#                    column_filters={"rmag":
#                                    ("<%f" % maxmag)},
#                    row_limit=maxsources)
    vquery = Vizier(columns=['objID', 'RAJ2000', 'DEJ2000',
                             'e_RAJ2000', 'e_DEJ2000',
                             'gmag', 'e_gmag',
                             'rmag', 'e_rmag',
                             'imag', 'e_imag',
                             'zmag', 'e_zmag',
                             'ymag', 'e_ymag'],
                    column_filters={"rmag":
                                    ("<%f" % maxmag)},
                    row_limit=maxsources)

    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg,
                           unit=(u.deg, u.deg),
                           frame='icrs')
    return vquery.query_region(field,
                               width=("%fd" % rad_deg),
                               catalog="II/349/ps1")[0]
