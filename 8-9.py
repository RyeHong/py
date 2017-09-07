import sqlite3
# Select and print all columns from the book table in order of publication.
conn = sqlite3.connect('book.db')
curs = conn.cursor()

curs.execute('SELECT * from books ORDER BY year')
print(curs.fetchall())