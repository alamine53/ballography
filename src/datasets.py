import os 
import pandas as pd
import requests
import zipfile
import io
import mysql.connector
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
    
    def __init__(self):
        self.conn = db_conn
        self.table_name = "dev_shots"
        
    def get_player_list(self):
        query = f"SELECT DISTINCT name, noahId FROM {self.table_name}"
        return pd.read_sql(query, self.conn)
    
    def shots_by_player(self, name, start_date, end_date):
        """ date is a string in the format YYYY-MM-DD"""
        query = """
        SELECT *
        FROM dev_shots
        WHERE name = %s
        AND date BETWEEN %s AND %s
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (name, start_date, end_date))
        colnames = [desc[0] for desc in cursor.description] 
        return pd.DataFrame(cursor.fetchall(), columns=colnames)
    
    def team_shots_by_period(self, start_date, end_date):
        """ returns the number of shots (except layups and free throws) and percentage over a given period 
        for all registered players
        Note: noahId is returned as a string (instead of scientific notation)
        """
        query = """
        SELECT name, CAST(noahId AS CHAR) as noahId, MIN(date) as min_date, MAX(date) as max_date, sum(made) as makes, count(*) as shots,sum(made)/count(*) as pct
        FROM dev_shots
        WHERE date BETWEEN %s AND %s
        AND layup = 0
        AND tagName != 'Free Throw'
        GROUP BY name, noahId
        ORDER by pct desc
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (start_date, end_date))
        colnames = [desc[0] for desc in cursor.description] 
        return pd.DataFrame(cursor.fetchall(), columns=colnames)


class Games(object):
    
    def __init__(self, season):
        self.season = season_to_year(season)
        self.conn = db_conn
        self.table_name = "game_players"
    
    def get_latest(self, last_n_days=10):
        """ get most recent games of all types (pre-season, regular season, playoffs)
        last_n_days: number of days to return
        """
        query = f"""
        SELECT date, season, seasonType, nbaGameId, nbaTeamId, team as homeTeam, opponentId, opponent as awayTeam, teamPts as homePts, oppPts as awayPts, teamMargin as homeMargin
        FROM {self.table_name}
        WHERE date > DATE_SUB(CURDATE(), INTERVAL {last_n_days} DAY)
        AND isHome = 1
        GROUP BY nbaGameId
        ORDER BY date ASC
        """
        return pd.read_sql(query, self.conn)
        
if __name__ == "__main__":
    print(season_to_year("2023-24"))