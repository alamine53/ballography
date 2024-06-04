import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

class Histogram3D:
    
    def __init__(self, bins=25, threshold=50, multiplier=10, zlim=4000, azimuth=42, elevation=25, unit='inch', alpha=0.50):
        self.bins = bins # Number of squares in the x and y dimensions
        self.threshold = threshold # Squares with a volume below this threshold will be empty
        self.multiplier = multiplier # Multiplier for the size of the squares (if bins are changed, this should be adjusted)
        self.zlim = zlim # Maximum volume of a square
        self.azimuth = azimuth
        self.elevation = elevation
        self.unit = unit
        self.alpha = alpha  # Transparency of the squares
        
    def plot(self, x, y, color='#e9e9e9', ax=None):
        
        # If an axes object isn't provided to plot onto, just get current one
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')

        # Construct the 2D histogram
        hist, xedges, yedges = np.histogram2d(x, y, bins=self.bins, range=[[-250, 250], [-47.5, 400]])
        
        # Apply the threshold
        hist[hist < self.threshold] = 0

        # Construct arrays for the anchor positions of the 16 bars.
        xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
        xpos = xpos.ravel()
        ypos = ypos.ravel()
        zpos = 0

        # Construct arrays with the dimensions for the 16 bars.
        dx = dy = self.multiplier * np.ones_like(xpos)
        dz = hist.ravel()

        # Filter out the bars where dz is 0
        nonzero = dz > 0
        xpos = xpos[nonzero]
        ypos = ypos[nonzero]
        dx = dx[nonzero]
        dy = dy[nonzero]
        dz = dz[nonzero]

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', alpha=self.alpha, color=color)
        ax.axis('off')
        # ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.3)
        ax.set_xlim(-250,250)
        ax.set_ylim(400,-47.5)
        ax.set_zlim(0, self.zlim)
        ax.view_init(azim=self.azimuth, elev=self.elevation)
        
        return ax

if __name__ == "__main__":
    
    # Create some data
    x = np.random.normal(-200, 200, 1000)
    y = np.random.normal(-22.5, 300, 1000)
    
    # Create the 3D histogram
    hist3d = Histogram3D()
    hist3d.plot(x, y)
    plt.show()
    