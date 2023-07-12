# Duck Typing = Concept where the class of an object is less important than the methods
#               class type is not checked if minimum methods/ attributes are present
#               "if it walks like a duck, and quacks like a duck, then it must be a duck

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")

class Chicken:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck1 = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)