import sqlite3

conn = sqlite3.connect('./example.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM test;')

result = cursor.fetchall()

print(result)