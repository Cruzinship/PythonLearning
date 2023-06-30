# exception = events detected during execution that interrupt the flow of a porgram

try:
    numerator = int(input("Enter a number to divdie: "))
    demoninator = int(input("Enter a number to divide by: "))
    result = numerator / demoninator
except ZeroDivisionError as e:
    print(e)
    print("you cant divid by zero retarded!")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("No matter what this executes")