#multiple inheritance = when a child class is derived from more than one parent class

class Pray:
     def flee(self):
         print("This aniamal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Pray):
    pass

class Hawk(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()