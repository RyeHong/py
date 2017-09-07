# Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol':
# 'H', 'number': 1. Then, create an object called hydrogen from class Element using
# this dictionary.




# class Element():
#     name = 'Hydrogen'
#     symbol = 'H'
#     number = 1

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = { 'name' : 'Hydrogen',
             'symbol':'H',
             'number':1}

print(Element(hydrogen['name'], "H", 1))

