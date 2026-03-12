import sqlite3

conn = sqlite3.connect("database/voting.db")
cursor = conn.cursor()

# Create candidates table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
votes INTEGER DEFAULT 0
)
""")

# Create voters table
cursor.execute("""
CREATE TABLE IF NOT EXISTS voters (
phone TEXT PRIMARY KEY
)
""")

# Insert default candidates
cursor.execute("INSERT INTO candidates (name, votes) VALUES ('Candidate 1',0)")
cursor.execute("INSERT INTO candidates (name, votes) VALUES ('Candidate 2',0)")
cursor.execute("INSERT INTO candidates (name, votes) VALUES ('Candidate 3',0)")

conn.commit()
conn.close()

print("Database created successfully!")