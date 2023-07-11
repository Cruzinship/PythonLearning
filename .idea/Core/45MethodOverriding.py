#Method overriding occurs when you write down the same name for a method but change its output for that specific subclass
class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This animal is eating grass")

class Fish(Animal):
    pass

rabbit = Rabbit()
fish = Fish()

rabbit.eat()
fish.eat()