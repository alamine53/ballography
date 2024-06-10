import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def draw_3d_halfcourt(ax=None, color='black', lw=0.5, outer_lines=False, unit='inch', facecolor=None, edgecolor='black', alpha=0):
    ''''
    Draw a half basketball court in inches.
    '''
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
    # court boundaries
    x_min, x_max = -250, 250 # sideline to sideline
    y_min, y_max = -47.5, 422.5 # baseline to halfcourt
    verts = [[(x_min,y_min,0), (x_min,y_max,0), (x_max,y_max,0), (x_max,y_min,0), (x_min,y_min,0)]]
    oob = Poly3DCollection(verts, edgecolor=edgecolor, facecolor=facecolor, alpha=alpha, linewidth=lw)
    ax.add_collection3d(oob)
    # Create the various parts of an NBA basketball court

    # outer paint boundaries
    x_min, x_max = -80, 80 # width of the paint
    y_min, y_max = -47.5, 142.5 # height of the paint
    verts = [[(x_min,y_min,0), (x_min,y_max,0), (x_max,y_max,0), (x_max,y_min,0), (x_min,y_min,0)]]
    paint = Poly3DCollection(verts, edgecolor=edgecolor, linewidth=lw, alpha=0)
    ax.add_collection3d(paint)
    
    # inner paint boundaries
    x_min, x_max = -60, 60 # width of the paint
    y_min, y_max = -47.5, 142.5 # height of the paint
    verts = [[(x_min,y_min,0), (x_min,y_max,0), (x_max,y_max,0), (x_max,y_min,0), (x_min,y_min,0)]]
    paint = Poly3DCollection(verts, edgecolor=edgecolor, linewidth=lw, alpha=0)
    ax.add_collection3d(paint)
    
    # free throw top arc
    center = (0, 142.5)
    radius = 60
    theta_full = np.linspace(np.radians(-90), np.radians(90), 120)
    y = center[1] + radius * np.cos(theta_full)  # Along the width of the court
    x = center[0] + radius * np.sin(theta_full)
    z = np.zeros_like(y)
    verts = [list(zip(x, y, z))]
    free_throw_top_arc = Line3DCollection(verts, colors=edgecolor, linewidth=lw)
    ax.add_collection3d(free_throw_top_arc)
    
    # free throw bottom arc 
    center = (0, 142.5)
    radius = 60
    theta_full = np.linspace(np.radians(90), np.radians(270), 120)
    y = center[1] + radius * np.cos(theta_full)  # Along the width of the court
    x = center[0] + radius * np.sin(theta_full)
    z = np.zeros_like(y)
    verts = [list(zip(x, y, z))]
    free_throw_bottom_arc = Line3DCollection(verts, colors=edgecolor, linewidth=lw, linestyles='dashed')
    ax.add_collection3d(free_throw_bottom_arc)
    
    # three point arc
    center = (0, 0)
    radius = 237.5
    theta_full = np.linspace(np.radians(-68), np.radians(68), 120)
    y = center[1] + radius * np.cos(theta_full)  # Along the width of the court
    x = center[0] + radius * np.sin(theta_full)
    z = np.zeros_like(y)
    verts = [list(zip(x, y, z))]
    three_point_arc = Line3DCollection(verts, colors=edgecolor, linewidth=lw)
    ax.add_collection3d(three_point_arc)
    
    # three point corner (left)
    x_min, x_max = -220, -220 # width of the corner
    y_min, y_max = -47.5, 92.5 # height of the corner
    verts = [[(x_min,y_min,0), (x_min,y_max,0), (x_max,y_max,0), (x_max,y_min,0), (x_min,y_min,0)]]
    corner = Poly3DCollection(verts, edgecolor=edgecolor, linewidth=lw, alpha=0)
    ax.add_collection3d(corner)
    
    # three point corner (right)
    x_min, x_max = 220, 220 # width of the corner
    y_min, y_max = -47.5, 92.5 # height of the corner
    verts = [[(x_min,y_min,0), (x_min,y_max,0), (x_max,y_max,0), (x_max,y_min,0), (x_min,y_min,0)]]
    corner = Poly3DCollection(verts, edgecolor=edgecolor, linewidth=lw, alpha=0)
    ax.add_collection3d(corner)
    
    # restricted area
    center = (0, 0)
    radius = 40
    theta_full = np.linspace(np.radians(-90), np.radians(90), 120)
    y = center[1] + radius * np.cos(theta_full)  # Along the width of the court
    x = center[0] + radius * np.sin(theta_full)
    z = np.zeros_like(y)
    verts = [list(zip(x, y, z))]
    restricted_area = Line3DCollection(verts, colors=edgecolor, linewidth=lw)
    ax.add_collection3d(restricted_area)

    ax.set_xlim(-250,250)
    ax.set_ylim(422.5,-47.5)

    # plot axis names
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    return ax


if __name__ == "__main__":
    
    draw_3d_halfcourt(outer_lines=True)
    plt.show()