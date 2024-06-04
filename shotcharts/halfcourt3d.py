import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def draw_halfcourt(ax=None, color='black', lw=1, outer_lines=False, unit='inch', facecolor='#F6E4CA', edgecolor='black', alpha=0.2):
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
    oob = Poly3DCollection(verts, edgecolor=edgecolor, facecolor=facecolor, alpha=alpha)
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
    
    # # Create the basketball hoop
    # # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # # 7.5 in our coordinate system
    # hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # # Create backboard
    # backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # # The paint
    # # Create the outer box 0f the paint, width=16ft, height=19ft
    # outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
    #                       fill=False)
    # # Create the inner box of the paint, widt=12ft, height=19ft
    # inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
    #                       fill=False)

    # # Create free throw top arc
    # top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
    #                      linewidth=lw, color=color, fill=False)
    # # Create free throw bottom arc
    # bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
    #                         linewidth=lw, color=color, linestyle='dashed')
    # # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    # restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
    #                  color=color)

    # # Three point line
    # # Create the side 3pt lines, they are 14ft long before they begin to arc
    # corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
    #                            color=color)
    # corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    
    # # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # # I just played around with the theta values until they lined up with the
    # # threes
    # three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
    #                 color=color)

    # # Center Court
    # center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
    #                        linewidth=lw, color=color)
    # center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
    #                        linewidth=lw, color=color)

    # # List of the court elements to be plotted onto the axes
    # court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
    #                   bottom_free_throw, restricted, corner_three_a,
    #                   corner_three_b, three_arc, center_outer_arc,
    #                   center_inner_arc]

    # if outer_lines:
    #     # Draw the half court line, baseline and side out bound lines
    #     outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
    #                             color=color, fill=False)
    #     court_elements.append(outer_lines)

    # # Add the court elements onto the axes
    # for element in court_elements:
    #     ax.add_patch(element)

    ax.set_xlim(-250,250)
    ax.set_ylim(422.5,-47.5)

    # plot axis names
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    return ax


if __name__ == "__main__":
    
    draw_halfcourt(outer_lines=True)
    plt.show()