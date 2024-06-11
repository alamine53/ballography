
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from geometry.court_2d import draw_halfcourt
from customization.headshots import get_player_img

class Heatmap:
        
        def __init__(self, cmap='plasma', thresh=0.25, alpha=0.75, headshot=True):
                self.cmap = cmap
                self.thresh = thresh
                self.alpha = alpha
                self.headshot = headshot
                
        def plot(self, x, y, ax=None, img_path=None, title=None, footnote=None, annos=None, nba_id=None):
                
                # If an axes object isn't provided to plot onto, just get current one
                if ax is None:
                        fig, ax = plt.subplots()
                
                g = sns.kdeplot(x=x, y=y,
                                fill=True, cbar=False, gridsize=100,
                                cmap=self.cmap, thresh=self.thresh, alpha=self.alpha)
                

                draw_halfcourt(ax, outer_lines=False)

                # customize the plot
                ax.set_title(title, fontweight='normal', color='black', loc='left') if title else None
                img_path = get_player_img(nba_id) if self.headshot and nba_id else None
                ax.imshow(img_path, extent=(115, 245, 414, 310), zorder=100) if img_path is not None else None
                if annos:
                        ax.text(-230, 405, annos,
                                color='black', ha='left', va='bottom', fontfamily='monospace', fontsize=8,
                                bbox=dict(facecolor='white', alpha=0.9, edgecolor='black'))

                # Add Data Scource and Author
                ax.text(-250,450,footnote, fontsize=8, fontfamily='monospace', color='black') if footnote else None

                # remove axis
                # ax.axis('off')
                # remove axis labels
                ax.set_xticks([])
                ax.set_yticks([])
                ax.set_xlabel('')
                ax.set_ylabel('')
                plt.savefig('heatmap.png', dpi=500, bbox_inches='tight')

                plt.show()