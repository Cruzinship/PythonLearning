try:
    with open("C:\\Users\\Gianpaulo\\OneDrive\\Documents\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

# Using with Open will close the files used.