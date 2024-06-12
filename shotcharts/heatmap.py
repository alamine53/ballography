
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from customization.headshots import get_player_img
try:
        from geometry.court_2d import draw_halfcourt
except ImportError:
        from ballography.geometry.court_2d import draw_halfcourt
class Heatmap:
        
        def __init__(self, cmap='plasma', thresh=0.25, alpha=0.75, headshot=True):
                self.cmap = cmap
                self.thresh = thresh
                self.alpha = alpha
                self.headshot = headshot
                
        def plot(self, x, y, ax=None, img_path=None, title=None, footnote=None, annos=None, nba_id=None, outfile=None):
                
                # If an axes object isn't provided to plot onto, just get current one
                if ax is None:
                        fig, ax = plt.subplots()
                
                g = sns.kdeplot(x=x, y=y,
                                fill=True, cbar=False, gridsize=100,
                                cmap=self.cmap, thresh=self.thresh, alpha=self.alpha)
                

                draw_halfcourt(ax, outer_lines=False)

                # customize the plot
                # ax.set_title(title, fontweight='bold', color='black', loc='left') if title else None
                # Split the title into main title and subtitle
                main_title, subtitle = title.split('\n')

                # Set the main title
                # ax.text(main_title, fontweight='bold', color='black', loc='left')
                ax.text(0.0, 1.07, main_title, transform=ax.transAxes, fontsize=16, fontweight='bold', color='black')

                # Add the subtitle with different font properties
                ax.text(0.0, 1.02, subtitle, transform=ax.transAxes, fontsize=10, style='normal', color='black', fontfamily='monospace')

                img_path = get_player_img(nba_id) if self.headshot and nba_id else None
                left_x, right_x, lower_y, upper_y = 80, 250, 415, 290
                ax.imshow(img_path, extent=(left_x, 250, 415, upper_y), zorder=100) if img_path is not None else None
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
                if outfile:
                        plt.savefig(outfile, dpi=400, bbox_inches='tight')

                plt.show()
                
if __name__ == "__main__":
        
    
    fig = plt.figure()
    ax = fig.add_subplot()
    map = Heatmap()
    x= np.random.normal(-200, 200, 1000)
    y = np.random.normal(0, 300, 1000)
    map.plot(x, y, ax=ax, nba_id=202681, title='Kyrie Irving', footnote='Data Source: NBA.com', annos='2021-2022 Season')
    plt.show()
    