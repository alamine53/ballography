import argparse 
import os
import pandas as pd
from tabulate import tabulate
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from src.datasets import Noah
from src.charts.geometry.court_2d import draw_halfcourt

def main():
    parser = argparse.ArgumentParser(
        "Display shot map for a player from Noah over the last N days. "    
        "By default, the output is saved to the current working directory."
    )
    parser.add_argument("-p", "--player", help="Player name", required=True, type=str)
    parser.add_argument("-l", "--last", help="Number of days to go back", default=30, type=int)
    parser.add_argument("-o", "--outdir", help="Output Directory", default="data", type=str)
    args = parser.parse_args()

    # create output directory if it doesn't exist
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    today = datetime.now()
    start_date = today-timedelta(days=args.last)
    outfile = f"{args.outdir}/{args.player.replace(' ', '')}_{start_date.strftime('%Y-%m-%d')}_{today.strftime('%Y-%m-%d')}.csv"
    
    if not os.path.exists(outfile):
        noah = Noah()
        df = noah.shots_by_player(
            name=args.player,
            start_date=start_date.strftime("%Y-%m-%d"), 
            end_date=today.strftime("%Y-%m-%d"))

        # save to csv
        df.to_csv(outfile, index=False)
    
    # read csv
    df = pd.read_csv(outfile)
    
    # plot shot map
    fig, ax = plt.subplots()
    draw_halfcourt(ax=ax)
    ax.scatter(df['floorLocX']*10, df['floorLocY']*10, alpha=0.5)
    
    # add title
    title = f"{args.player}\n{start_date.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}"
    ax.set_title(title, fontsize=14, fontfamily='monospace', color='black',
                loc='left')
    
    # add headshot
    plt.show()

if __name__ == "__main__":
    main()