# Licensed under a 3-clause BSD style license - see LICENSE.rst
import sys
import taco
from Quaternion import Quat
import numpy as np

# For testing with a simpler geometry
# slab_planes = taco.make_slab()
# slab_rads = taco.make_radiator2()

import numpy as np

def norm(vec):
    return vec / np.sqrt(np.sum(vec**2))

i = 0
# Chandra orbit position (ala orbit ephemeris X,Y,Z) (meters)
ra = 0.
dec = -90.0
for i, alt in enumerate(np.arange(1000e3, 1500e3, 1000e3)):
    p_chandra_eci = np.array([taco.Rad_Earth + alt, 0, 0]) 
    att = [ra, dec, 0.]
    vis, illum, rays = taco.calc_earth_vis(p_chandra_eci, att, ngrid=1000)
    print illum

    if 1:
        # figure(i)
        clf()
        blocked = vis == 0
        if len(blocked.nonzero()) > 0:
            pos = rays[blocked]
            plot(pos[:,1], pos[:,2], '.k')
        if len(vis) > 0:
            pos = rays[~blocked]
            plot(pos[:,1], pos[:,2], '.r')
        xlim(-1,1)
        ylim(-1,1)



