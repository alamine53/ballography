import numpy as np 
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def scatter_to_hexbins(x, y, gridsize=35, hex_size=7.5, thresh=[1,2,4],
                       **kwargs):
    ''' convert dots to hexbins with three different sizes depending on frequency.
    assume all the same color.
    to adjust the size of the hexagons, you will need to adjust both the gridsize and hex_size.
    thresh: list of minimum number of counts to be considered for small, medium, and large hexagons.
        i.e. less than 1 -> small hexagon, 1-2 -> medium hexagon, 2-4 -> large hexagon
    '''
    # use plt.hexbin to create a hexbin chart and extract the counts and vertices
    tmpfig = plt.figure()
    axtemp = tmpfig.add_subplot(111)
    poly_hexbins = axtemp.hexbin(x,y, gridsize=gridsize, extent=[-250,250,-62.5,500-62.5])
    counts = poly_hexbins.get_array()
    verts = poly_hexbins.get_offsets()
    plt.close(tmpfig) # we don't need it anymore

    # create hexagons
    xy = hex_size*np.array([np.cos(np.linspace(np.pi/6,np.pi*330/180,6)),np.sin(np.linspace(np.pi/6,np.pi*330/180,6))]).T
    b = np.zeros((6,2))

    # adjust size per hexagon based on shot volume
    binsizes = np.zeros_like(counts)
    binsizes[counts>=thresh[2]] = 1 # full size hexagon
    binsizes[(counts<thresh[2]) & (counts>=thresh[1])] = 0.7 # medium size hexagon
    binsizes[(counts<thresh[1]) & (counts>=thresh[0])] = 0.4 # small hexagon

    patches = []
    for offc in range(len(verts)):
        if binsizes[offc] != 0:
            xc,yc = verts[offc][0],verts[offc][1] # vertex center
            b[:,0] = xc + xy[:,0]*binsizes[offc]
            b[:,1] = yc + xy[:,1]*binsizes[offc]

            patches.append(Polygon(b.copy(), closed=True))
    p = PatchCollection(patches, edgecolors='black', linewidths=0.5, zorder=200, **kwargs)
    return p, counts, verts