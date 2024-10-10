import os 
import argparse
from tabulate import tabulate
from datetime import datetime
import pandas as pd
from src.datasets import Games

def main():
    parser = argparse.ArgumentParser("Get the latest scores")
    parser.add_argument("-s", "--season", help="Season", default="2023-24")
    parser.add_argument("-l", "--last", help="Number of days", default=3)
    parser.add_argument("-r", "--replace", help="Replace the existing file", action="store_true")
    args = parser.parse_args()
    
    today = datetime.now().strftime("%Y-%m-%d")
    outfile = f"data/scores_last_{args.last}_days_{today}.csv"
    
    print(f"Getting latest scores for the last {args.last} days")
    if not os.path.exists(outfile) or args.replace:
        
        games = Games(season=args.season)
        df = games.get_latest(last_n_days=args.last)
        df.to_csv(outfile, index=False)
        print(f"Latest scores saved to {outfile}")
    
    df = pd.read_csv(outfile)
    print(tabulate(df, headers='keys', tablefmt='psql'))
    
if __name__ == "__main__":
    main()