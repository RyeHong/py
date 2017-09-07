# Call print(hydrogen). In the definition of Element, change the name of method
# dump to __str__, create a new hydrogen object, and call print(hydrogen) again.

class Element():

    # name = 'Hydrogen'
    # symbol = 'H'
    # number = 1
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
       return self.name



# hydrogen = Element.__str__(Element)
print(Element("A", "B", "C"))