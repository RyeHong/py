import sqlite3
# Select and print the title column from the book table in alphabetical order.
conn = sqlite3.connect('book.db')
curs = conn.cursor()

curs.execute('SELECT title from books ORDER BY title')
print(curs.fetchall())