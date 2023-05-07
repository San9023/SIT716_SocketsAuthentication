import sqlite3
import hashlib


conn = sqlite3.connect("credentials.db")
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS data (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "Sangeeth", hashlib.sha256(
    "s222434398".encode()).hexdigest()
username2, password2 = "iamsan", hashlib.sha256(
    "san".encode()).hexdigest()

cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username1, password1))
cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username2, password2))

conn.commit()