import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

print(cur.execute("SELECT * FROM prompts").fetchall())

connection.commit()
connection.close()