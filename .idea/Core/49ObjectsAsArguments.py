class Car:

    color = None

class Motorcycle:

    color = None

def changeColor(vehicle, color):
   vehicle.color = color


car1 = Car()
car2 = Car()
car3 = Car()
motorcycle1 = Motorcycle()

changeColor(car1, "Orange")
changeColor(car2, "Blue")
changeColor(car3, "White")
changeColor(motorcycle1, "Black")

print(car1.color)
print(car2.color)
print(car3.color)
print(motorcycle1.color)