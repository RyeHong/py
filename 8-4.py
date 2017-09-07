import csv

import csv
# Save these text lines to a file called books.csv. Notice that if the fields are separated
# by commas, you need to surround a field with quotes if it contains a comma.
word = 'author,book \
J R R Tolkien,The Hobbit \
Lynne Truss,"Eats, Shoots & Leaves"'

with open('D://books.csv','wt') as file:

    file.write(word)




with open('D://books.csv','rt') as fout:
    books = csv.DictReader(fout)
    villains = [row for row in books]

print(villains)

