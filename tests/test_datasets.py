import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.datasets import Games, Shots, Noah

def test_games():
    games = Games(season="2023-24")
    assert games.games is not None
    assert len(games.games) > 0

if __name__ == "__main__":
    test_games()