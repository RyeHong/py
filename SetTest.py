print(set(['Dasher','Dancer','Prancer','Mason-Dixon']))

print(set(('Ummagumma','Echoes','Atom Heart Mother')))

print(set({'apple':'red','orange':'orange','cherry':'red'}))

drinks = {
        'martini': {'vodka','vermouth'},
        'black russian':{'vodka','kahlua'},
        'white russian':{'cream','kahlua','vodka'},
        'manhattan':{'rye','vermouth','bitters'},
        'screwdriver':{'orange juice','vodka'}

}
print("#########")

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print("#########")

for name,contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
print("#########")

for name ,contents in drinks.items():
    if contents & {'vermouth','orange juice'}:
        print(name)
print("#########")

for name,contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth','cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

print("#########")

for name,contents in drinks.items():
    if 'black russian' in name:
        print(contents)

a = {1,2}
b = {2,3}

print('a&b',a&b)

print('a&b another use',a.intersection(b))

print('bruss & wruss',bruss & wruss)

print('a|b union',a|b)

print('a|b another use',a.union(b))

print('a-b difference',a-b)

print('a-b difference another use',a.difference(b))

print('a^b items in one set or the other,but not both',a^b)

print('a^b symmetric_difference()',a.symmetric_difference(b))

print('a <= b subset',a <= b)

print('a <=b subset another use',a.issubset(b))

print('a < b proper subset',a < b)

print('#####')

marx_list = ['Groucho','Chico','Harpo']

marx_tuple = 'Groucho','Chico','Harpo'

marx_dict = {'Groucho':'banjo','Chico':'piano','Harpo':'harp'}

print('marx_list[2]',marx_list[2])

print('marx_tuple[2]',marx_tuple[2])

print('marx_dict["Harpo"]',marx_dict['Harpo'])

print('########')

marxes = ['Groucho','Chico','Harpo']
pythons = ['Chapman','Cleese','Gilliam','Jones','Palin']
stooges = ['Moe','Curly','Larry']

tuple_of_lists = marxes,pythons,stooges

print('tuple_of_lists',tuple_of_lists)


print('########')
list_of_lists = [marxes,pythons,stooges]

print('list_of_lists',list_of_lists)

print('########')

dict_of_lists = {'Marxes':marxes, 'Pythons':pythons, 'Stooges':stooges}

print('dict_of_lists',dict_of_lists)


count = 1

print('########')
while count <= 5:
    print(count)
    count += 1

print('########')

# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())


print('########')

# while True:
#     value = input("Integer,please [q to quit]")
#     if value == 'q':
#         break
#
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number,"squared is",number*number)

print('########')

numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0 :
        print('Found even number',number)
        break
    position += 1
else:
    print('No even number found')

print('########')

rabbits = ['Flopsy','Mopsy','Cottontail','Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

print('########')

for rabbit in rabbits:
    print(rabbit)

print('########')

word = 'cat'
for letter in word:
    print(letter)

print('########')

accusation = {'room':'ballroom','weapon':'lead pipe','person':'Col.Mustard'}

for card in accusation:
    print(card)

print('########')

for card,contents in accusation.items():
    print('Card',card,'has the contents',contents)

print('########')

days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']

for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,":drink",drink,"- eat",fruit,"- enjoy",dessert)

print('########')

english = 'Monday','Tuesday','Wednesday'
french = 'Lundi','Mardi',"Mercredi"

print(list( zip(english,french)))

print(dict( zip(english,french)))




