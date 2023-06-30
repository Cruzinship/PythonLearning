#Loop Control statements = change a loops execution from its normal sequence

# break =      used to terminate the loop entirely
# continue =   skips to the next iteration of the loop
# pass =       does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "": #if name has a value other than empty then break
     break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-": #We used continue here in order to skip every dash within our String
        continue
    print(i, end="") #How to print it all on one line

for i in range(1,21): # Remember second number is exclusive here
    if i == 13:
        pass
    else:
        print(i)
