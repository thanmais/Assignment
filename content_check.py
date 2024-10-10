import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('news_articles.db')
cursor = conn.cursor()

# Query the articles stored in the database
cursor.execute("SELECT * FROM articles")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
