from openai import OpenAI
import pandas as pd
import os 
import argparse

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--player", type=str, default="Luka Doncic")
    args = parser.parse_args()
    return args

def create_shooting_stats_table(df) -> pd.DataFrame:
    games_by_player = df.groupby(['PLAYER_NAME', 'GAME_ID']).agg(makes=('SHOT_MADE', 'sum'), attempts=('EVENT_TYPE', 'count')).reset_index()
    games_by_player = games_by_player.groupby('PLAYER_NAME').agg({'GAME_ID':'count', 'makes':'sum', 'attempts':'sum'})
    n_games = games_by_player['GAME_ID'].rename('N_games')
    stats = df.groupby(['PLAYER_NAME', 'BASIC_ZONE']).agg(makes=('SHOT_MADE', 'sum'), attempts=('EVENT_TYPE', 'count'))
    stats['fg_pct'] = round(100 * stats['makes'] / stats['attempts'], 1)
    stats = stats.reset_index().merge(n_games, on='PLAYER_NAME')
    stats['att_per_game'] =round(stats['attempts'] / stats['N_games'],2)
    stats['shot_rate_pctile'] = stats.groupby('BASIC_ZONE')['att_per_game'].transform(lambda x: x.rank(pct=True)).round(2)
    stats['fgp_pctile'] = stats.groupby('BASIC_ZONE')['fg_pct'].transform(lambda x: x.rank(pct=True)).round(2)
    stats = stats[["PLAYER_NAME", "BASIC_ZONE", "att_per_game",  "shot_rate_pctile", "fg_pct", "fgp_pctile"]]
    return stats

def main():
    args = get_args()
    player_name = args.player
    df = pd.read_csv("NBA_2024_Shots.csv")
    shooting_stats = create_shooting_stats_table(df)
    df_player = df[df['PLAYER_NAME'] == player_name]
    nba_id = df_player['PLAYER_ID'].values[0]
    position = df_player['POSITION'].unique()[0]
    team = df_player['TEAM_NAME'].unique()[0]
    individual_stats = shooting_stats[shooting_stats["PLAYER_NAME"] == player_name].drop("PLAYER_NAME", axis=1).set_index("BASIC_ZONE")
    

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a professional basketball scout."},
        {"role": "user", "content": prompt},
        ],
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()