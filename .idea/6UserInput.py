name = input("What is your name?: ") #Takes a string
age = int(input("How old are you?: ")) #Takes a Integer
month = int(input("What month were you born?: "))
day = int(input("What day were you born?: "))
year = int(input("What year is it currenntly?: "))
IforNot = str(input("Has your birthday already happened?: "))
#Difference from Java. In java we would have to call a Scanner class
#then we print the message seperated from the input which we also write differently
#For python we simply typeCast to change how our input takes data

IforNot.lower()
age = age + 1
print("Hello "+ name)

if (IforNot == 'yes') :
     print("Your birthdays already passed on "+ str(month) + "-" + str(day) + "-" + str(year) +" which makes you " + str(age) +" already")
else:
    print("You will be " + str(age) + " years old on your incoming birthday on " + str(month) + "-" + str(day) + "-" + str(year))




