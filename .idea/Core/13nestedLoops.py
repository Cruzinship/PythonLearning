# nested loops = The "inner loop" will finish all of it's iterations before
                 # finishing one iteration of the "outer loop"
rows = int(input("How many rows? "))
columns = int(input("How many columbs? "))

symbol = input("Enter a symbol to use: ")


for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #end is used to end the nested loop
    print()