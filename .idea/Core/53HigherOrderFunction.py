# Higher Order Function = a function that either:
# 1. Accepts a function as an argument
# 2. returns a function
#   (In python, functions are also treated as objects)
#
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

def anything(func): #Dynamic version of function above
    text = input("Enter whatever sentence ya want: ")
    funcText = func(text)
    print(funcText)

hello(loud)
hello(quiet)
anything(loud)
anything(quiet)