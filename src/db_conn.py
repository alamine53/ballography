import os
import dotenv
import mysql.connector

dotenv.load_dotenv()

print(os.getenv("DB_HOST"))
print(os.getenv("DB_NAME"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))
print(os.getenv("DB_PORT"))

db_conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"))
