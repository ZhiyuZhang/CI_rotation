import glob, re, os, copy

import numpy as np
from   astropy.io import fits
from   astropy    import wcs
import astropy.units as u
from   astropy.coordinates import ICRS

import matplotlib.pyplot as plt
import aplpy




file =  'fitsfile/continuum.fits'

if os.path.isfile(file) == True:
     image         =  fits.open(file)[0]
     header        =  image.header
     w             =  wcs.WCS(header, image)
     image_data    =  image.data


plt.clf()

fig = plt.figure(figsize                       = (9, 6))
f   = aplpy.FITSFigure(file,    figure = fig)
f.show_grayscale(vmin=-0.2E-3, vmax=1E-2,invert=True)
f.savefig('test.pdf')
