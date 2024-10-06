
# define color scheme
color_mapping = {0: 'gray', 1: 'blue'}

# plot shots
fig, ax = plt.subplots()
draw_court(ax, outer_lines=False)

# Map categorical outcome to colors
colors = df_player['outcome'].map(color_mapping)
dots = ax.scatter(df_player['locX'], df_player['locY'], c=colors, s=30, alpha=0.35, zorder=10, edgecolors=None)

# add player image
player_id = df_player['nbaId'].values[0]
img_path = get_player_img(player_id)
ax.imshow(img_path, extent=(115, 245, 414, 310), zorder=100)

# add a title
ax.set_title('Luka Doncic \n2023-24 Reg. Season', fontweight='normal', color='black', loc='left')

# add the previously calculated percentages as annotations
ax.text(-230, 405, 'FG  {:.1%} \n3PT {:.1%}\n2PT {:.1%}'.format(fgp, fg3p, fg2p),
        color='black', ha='left', va='bottom', fontfamily='monospace', fontsize=8,
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='black'))

# Add Data Scource and Author
ax.text(-250,450,'Data: stats.nba.com'
        '\nAuthor: MCF AI Bootcamp 2024',
        fontsize=8, fontfamily='monospace', color='black')

# remove axis
# ax.axis('off')
# remove axis labels
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('scatter.png', dpi=500, bbox_inches='tight')
plt.show()