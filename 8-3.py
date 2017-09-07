import csv
# Save these text lines to a file called books.csv. Notice that if the fields are separated
# by commas, you need to surround a field with quotes if it contains a comma.
word = 'author,book \
J R R Tolkien,The Hobbit \
Lynne Truss,"Eats, Shoots & Leaves"'

list = []
w = word.split(',')
for a in w:
    list.append('"'+ a + '"')

with open('D://books.csv','wt') as file:

    file.write(str(list))



