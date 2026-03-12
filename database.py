import sqlite3

conn = sqlite3.connect("database/voting.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT,
role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
party TEXT,
votes INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS votes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
candidate_id INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")