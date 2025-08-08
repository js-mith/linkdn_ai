import sqlite3
import pandas as pd

DB_FILE = "data/posts.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        date TEXT,
        content TEXT
    )
    """)
    conn.close()

def save_post(date, content):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO posts VALUES (?, ?)", (str(date), content))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    conn.close()
    return df
