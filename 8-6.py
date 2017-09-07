import sqlite3
# Use the sqlite3 module to create a SQLite database called books.db, and a table
# called books with these fields: title (text), author (text), and year (integer).
conn = sqlite3.connect('book.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
                (title VARCHAR(20) ,
                author VARCHAR(50),
                year INT)''')

