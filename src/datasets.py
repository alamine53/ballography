import os 
import pandas as pd
import requests
import zipfile
import io
from datetime import datetime
from src.db_conn import db_conn

def season_to_year(season):
    if "-" in season:
        return str(season.split("-")[0][:2]) + str(season.split("-")[1][-2:])
    else:
        return season

class Shots(object):
    
    def __init__(self, season, indir="data", from_db=False):
        self.season = season_to_year(season)
        self.conn = db_conn
        self.table_name = "event_pbp"
        self.indir = indir
        if from_db:
            self.shots = self.load_from_db()
        else:
            self.shots = self.load_from_csv()

    def load_from_csv(self):
        filepath = self.indir + "/NBA_" + self.season + "_Shots.csv"
        if not os.path.exists(filepath):
            # download the file from the website
            url = f"https://github.com/DomSamangy/NBA_Shots_04_24/raw/main/data/NBA_{self.season}_Shots.csv.zip"
            try:
                # Download the zip file
                response = requests.get(url)
                response.raise_for_status()  # Raises an HTTPError for bad responses
                
                # Extract the contents of the zip file
                with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                    zip_ref.extractall('.')
                
                print("NBA data downloaded and extracted successfully.")
            
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while downloading the file: {e}")
            except zipfile.BadZipFile:
                print("The downloaded file is not a valid zip file.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        self.shots = pd.read_csv(filepath)
        return self.shots
    
    def load_from_db(self):
        query = f"SELECT * FROM {self.table_name} WHERE season={self.season}"
        return pd.read_sql(query, self.conn)
    
    def get_player_shots(self, player_name):
        return self.shots[self.shots['PLAYER_NAME'] == player_name]
    
    def get_team_shots(self, team_name):
        return self.shots[self.shots['TEAM_NAME'] == team_name]
    
    def get_opponent_shots(self, opponent_name):
        return self.shots[self.shots['OPPONENT_NAME'] == opponent_name]
    
    
class Noah(object):
    
    def __init__(self, season, from_db=True):
        self.season = season
        self.conn = db_conn
        self.table_name = "dev_shots"
    
    def player_shots_by_period(self, player_name, start_date, end_date):
        query = f"SELECT * FROM {self.table_name} WHERE PLAYER_NAME = '{player_name}' AND GAME_DATE >= '{start_date}' AND GAME_DATE <= '{end_date}'"
        return pd.read_sql(query, self.conn)
    
    def team_shots_by_period(self, team_name, start_date, end_date):
        query = f"SELECT * FROM {self.table_name} WHERE TEAM_NAME = '{team_name}' AND GAME_DATE >= '{start_date}' AND GAME_DATE <= '{end_date}'"
        return pd.read_sql(query, self.conn)
    
    def get_player_list(self):
        query = f"SELECT DISTINCT PLAYER_NAME FROM {self.table_name}"
        return pd.read_sql(query, self.conn)

class Games(object):
    
    def __init__(self, season):
        self.season = season_to_year(season)
        self.conn = db_conn
        self.table_name = "game_players"

    def __load_games(self):
        self.games = pd.read_sql(f"SELECT * FROM {self.table_name} WHERE season={self.season}", self.conn)
        return self.games
    
    def get_latest(self, last_n=10):
        """ get most recent games of all types (pre-season, regular season, playoffs)"""
        query = f"SELECT * FROM {self.table_name} ORDER BY date DESC LIMIT {last_n}"
        return pd.read_sql(query, self.conn)
        
if __name__ == "__main__":
    print(season_to_year("2023-24"))