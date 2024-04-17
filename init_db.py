import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO prompts (reflection, msg) VALUES ('This is a test reflection.', 'This is a test message.')")

connection.commit()
connection.close()