import sqlite3
import csv
# Read books.csv and insert its data into the book table.
conn = sqlite3.connect('book.db')
curs = conn.cursor()
with open('D://book.csv','rb') as fread:
       reader = csv.reader(fread)

       for field in reader:
              curs.execute("INSERT INTO books VALUES (?,?,?);", field)

