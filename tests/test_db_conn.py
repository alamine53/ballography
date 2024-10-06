import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db_conn import db_conn

def test_db_conn():
    assert db_conn is not None

if __name__ == "__main__":
    test_db_conn()