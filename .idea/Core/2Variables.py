# Variables
# python will auto assign variable types to variables depending on their input
# Cool note puting Type before the value of the varibale in a print statement it can tell you its type
variableNum = 10
variableString = 'I am Happy'
print(variableNum)
print(variableString)
FirstName = "Bro"
LastName = "Code"
FullName = FirstName + " " + LastName
print("Hello "+ FullName)
print(type(FirstName))
print('------------------------------------------------')
# ------------------------------------------------------
# Understanding Operators, and doing simple math
# Int data type
Num1 = 1
Num2 = 2
Num3 = 3
Num4 = 4
age = 18
age += 1
NumSum = Num3 * Num4
NumSum2 = Num2 - Num1
NumSum3 = Num4 + Num2
NumSum4 = NumSum3 / NumSum2
print(type(NumSum))
print(NumSum2)
print(NumSum3)
print(NumSum4)
print(age)
print(type(age))
print("---------------------------------------------------")
# Float
NumFloat = 19.99
print(NumFloat)
print(type(NumFloat))
print("------------------------------------------------------------")
# Boolean
TrueBoolean = True
FalseBoolean = False
print(TrueBoolean)
print(FalseBoolean)
# Multiple assignment
SpoongeBob = Patrick = Sandy = Squidward = 30
print(SpoongeBob)
print(Patrick)
print(Sandy)
print(Squidward)
# You can even assign differe data types thier values with this method. It can space and time
name, age, attractive = "Bro", 21, True
print(name)
print(age)
print(attractive)