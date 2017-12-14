import glob, re, os, copy
import numpy as np
import matplotlib.path
from   astropy.io import fits
from   astropy    import wcs
import astropy.units as u
from   scipy.interpolate   import UnivariateSpline, SmoothBivariateSpline
from   astropy.coordinates import ICRS
import matplotlib.pyplot as plt
import pyfits


file =  'fitsfile/continuum.fits'

if os.path.isfile(file) == True:
     image         =  fits.open(file)[0]
     header        =  image.header
     w             =  wcs.WCS(header, image)
     image         =  image.data




