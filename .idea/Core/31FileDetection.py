import os

path1 = "C:\\Users\\Gianpaulo\\OneDrive\\Documents\\Desktop\\test.txt"
path =  "C:\\Users\\Gianpaulo\\OneDrive\\Documents\\Desktop\\folder"
if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist")
