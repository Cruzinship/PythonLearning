# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))
#if statement formula if condition :
#Block of Code
#elif condition:
#Block of code
#else:
#Block of code
if age == 100:
    print("You are a century old:")
elif age == 10:
    print("You are a decade old:")
elif age >= 11 and age <= 21:
    print("You are older than a child, but younger than an adult")
elif age >= 21 and age < 99:
    print("You are an adult")
elif age < 0: #elif is the equivilant of else if in java
    print("You haven't been born yet:")
else: #Ending Statement
    print("You are a child")