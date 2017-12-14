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

f.show_contour(file,  levels=[0.0003,0.0004,0.0006,0.0008,0.001,0.002],colors=['red',  'red', 'red', 'red', 'red', 'red'],overlap=True)
f.set_frame_color('black')
f.set_tick_labels_font(size='12')
f.set_axis_labels_font(size='15')
f.set_tick_labels_format(xformat='hh:mm:ss',yformat='dd:mm:ss')
f.set_axis_labels(xlabel='R.A. (J2000)', ylabel='Dec. (J2000)', xpad='default', ypad='default')
f.set_tick_color('black')
f.show_colorbar()
fig.text(0.27 ,0.85 ,'test', color='black', size='12')

f.savefig('test.pdf')


