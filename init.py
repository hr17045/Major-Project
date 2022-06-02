import sqlite3
conn = sqlite3.connect('login.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE details (id INTEGER PRIMARY KEY, name char(100) NOT NULL, password bool NOT NULL)")

conn.commit()