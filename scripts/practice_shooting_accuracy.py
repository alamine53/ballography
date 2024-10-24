import argparse 
from tabulate import tabulate
from datetime import datetime, timedelta
from src.datasets import Noah

def main():
    parser = argparse.ArgumentParser(
        "Shot stats by player from the practice facility over the last N days via Noah"
    )
    parser.add_argument("-l", "--last", help="Number of days to go back", default=30, type=int)
    args = parser.parse_args()

    today = datetime.now()
    start_date = today-timedelta(days=args.last)
    noah = Noah()
    df = noah.team_shots_by_period(
        start_date=start_date.strftime("%Y-%m-%d"), 
        end_date=today.strftime("%Y-%m-%d"))
    print("Noah shots over the last", args.last, " days\nExcept Layups and Free Throws")
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    main()