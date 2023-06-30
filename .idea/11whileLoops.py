# while loop = a statement that will execute its block of codes as long as it's conditions remains true
# The Example of an infinite while loop
# while 1 == 1:
#     print("Help! Im stuck in a loop")
# This below would be an example of a never ending loop with a condition which needs to be filled to then end the loop

name = ""
while len(name) == 0:
    name = str(input("Enter your name: "))

print("Hello " + name)

# Two ways to solve
# The way below is more professional
name2 = None
while not name2:
    name2 = str(input("Enter your name: "))

print("Hello " + name2)
