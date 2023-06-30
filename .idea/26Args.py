# *args = parameter that will pack arguments into a tuple
#        useful so that a function can accept a varying amount of arguments
def add(*args):
    sum = 0 # Sum starts at zeor
    args = list(args)
    args[0] = 0
    args = tuple(args)
    for i in args: #add one after the other as we go through our tuple
        sum += i
    return sum

print(add(1,2,3,4,5,6))
#By default using *args all variables used are going to be put into a tuple
#If you ever wish to change the value of the elements within the tuple youd have to cast it into a list
#If you wish to to it back to being a tuple you can just with re casting it after wards, after the change is done