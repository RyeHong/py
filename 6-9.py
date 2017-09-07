# Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one
# method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or
# 'campers' (Octothorpe). Create one object from each and print what it eats.

class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octothorpe():
    def eats(self):
        return 'campers'


a = Bear()
print(a.eats())
b = Rabbit()
print(b.eats())
c = Octothorpe()
print(c.eats())

