import sqlite3

conn = sqlite3.connect('data/UsersPontuacao.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pontuation(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    pontos INTEGER)
""")
