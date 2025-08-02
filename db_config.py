# db_config.py
import os
from dotenv import load_dotenv
import psycopg2

# .env dosyasını oku
load_dotenv()

# Bağlantı oluştur
def connect_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    return conn
