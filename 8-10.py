import sqlalchemy as sa
# Use the sqlalchemy module to connect to the sqlite3 database books.db that you
# just made in exercise 8.6. As in 8.8, select and print the title column from the book
# table in alphabetical order
conn = sa.create_engine('sqlite:///C:\\Users\\SEL\\PycharmProjects\\untitled\\book.db')
con = conn.execute('SELECT title from books ORDER BY title')
for a in con:
    print(a)