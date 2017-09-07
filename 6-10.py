# Define these classes: Laser, Claw, and SmartPhone. Each has only one method:
# does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (Smart
# Phone). Then, define the class Robot that has one instance (object) of each of these.
# Define a does() method for the Robot that prints what its component objects do.

class Laser():
    def does(self):
        return 'disintegrate'
class Claw():
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'


class Robot(Laser,Claw,SmartPhone):
    a = Laser()
    b = Claw()
    c = SmartPhone()
    def does(self):
        print(self.a.does())
        print(self.b.does())
        print(self.c.does())

abc = Robot()
abc.does()


