import time
# for loop = a statement that will execute it's block of code
#            a limited amount of times
#
#            while loop = unlimited
#            for loop = limited
# Range function
for i in range(10): # How to print something 10 times. Java would be fori then state what you want the number to be
    print(i+1)

print("-----------------------------------------")

for i in range(50,100): # First is exclusive, Second is inclusive
    print(i)
print("-----------------------------------------")

name = "Gianpaulo"
for i in name:
    print(i)

print("-----------------------------------------")

#Countdown program
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")