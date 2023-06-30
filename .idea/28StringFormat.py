# str.format() = optional method that gives users
#                more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number)) #Gives decimal point and you can tell it how many it can have after
print("The number pi is {:,}".format(number)) # Gives the comma after every 3 0s
print("The number pi is {:b}".format(number)) # Writes it in binary
print("The number pi is {:o}".format(number)) # Octal Number
print("The number pi is {:X}".format(number)) # Hexadecimal
print("The number pi is {:E}".format(number)) # Scientific notation


#name = "Gianpaulo"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))


# animal = "cow"
# item = "moon"

# print("The "+ animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item))#Positional arguments
# print("The {animal2} jumped over the {animal2}".format(animal2="cow", item2="moon")) # Keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal,item))