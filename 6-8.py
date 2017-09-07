# Modify Element to make the attributes name, symbol, and number private. Define a
# getter property for each to return its value.


class Element():
    __name = 'Hydrogen'
    __symbol = 'H'
    __number = 1

    def getter_name(self):
        return self.__name

    def getter_symbol(self):
        return self.__symbol

    def getter_number(self):
        return self.__number


