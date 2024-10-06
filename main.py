import argparse 
import tabulate 

from src.datasets import Shots, Games
from src.charts.heatmap import Heatmap


def get_shooting_stats(df):
    df = df.copy()
    n_games = len(df['GAME_ID'].unique())
    stats = df.groupby('BASIC_ZONE').agg(attempts=('EVENT_TYPE', 'count'))
    stats['per_game']= stats['attempts'] / n_games
    # replace left corner 3 by corner 3
    stats = stats.reset_index()
    stats['BASIC_ZONE'] = stats['BASIC_ZONE'].replace('Left Corner 3', 'Corner 3')
    stats['BASIC_ZONE'] = stats['BASIC_ZONE'].replace('Right Corner 3', 'Corner 3')
    stats = stats[stats['BASIC_ZONE'] != 'Backcourt']
    stats = stats.groupby('BASIC_ZONE').sum().sort_values('attempts', ascending=False)
    stats.drop('attempts', axis=1, inplace=True)    
    return stats

def main():
    
    parser = argparse.ArgumentParser("Plot a heatmap of a player's shots")
    parser.add_argument("-p", "--player", help="Player name", default="Kyrie Irving")
    parser.add_argument("-s", "--season", help="Season", default="2023-24")
    parser.add_argument("-o", "--output", help="Output file", default=None)
    parser.add_argument("-c", "--csv_path", help="Path to the csv file", default="data/NBA_2024_Shots.csv")
    args = parser.parse_args()

    # games = Games(season=args.season)
    # print(games.get_latest())
    
    shots = Shots(season=args.season, from_db=False)
    print(shots.shots)
    
    hm = Heatmap(headshot=True)
    
    print("Player name: ", args.player)
    print("Season: ", args.season)
    print("Output file: ", args.output)
    print("CSV path: ", args.csv_path)
    
    dfp = shots.get_player_shots(args.player)

    stats = get_shooting_stats(dfp)
    annos = tabulate.tabulate(stats, headers= ["Attempts per game", ""], tablefmt="simple", floatfmt=".1f")   
    print(annos)
    nba_id = dfp['PLAYER_ID'].values[0]
    x, y = 10*dfp['LOC_X'], 10*dfp['LOC_Y']-47.5 # convert feet to inches
    hm.plot(x, y, title=f"{args.player}\n2023-24 Reg. Season", footnote="nba.stats.com", nba_id=nba_id, annos=annos)

if __name__ == "__main__":
    main()
