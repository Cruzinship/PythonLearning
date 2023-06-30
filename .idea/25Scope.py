# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created in
#         A global and locally scoped versions of a variable can be created

name = "Bro" # global scope (avaible inside and outside functions)
def displayName():
    name = "Code" # local scope (available only inside this functions for being defined within it)
    print(name) #This will print the local before the global if there is one created within the function

displayName()
print(name)

# L = Local
# E = Encoding
# G = Global
# B = Built-in