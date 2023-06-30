#index operator [] = gives access tp a sequence's element (str,list,tuples)

name = "gianpaulo Cruz!"
#Below is from the beggining to the index number 9
firstName = name[:9].upper() #Access elements zero to 3 and make them uppercase. NOTE first in inclusive and second is exclusive
lastName = name[10:14].lower() #Range
lastCharacter = name[-1] #Goes to the back

print(firstName)
print(lastName)
print(lastCharacter)




#Fun example  1
# if(name[0].islower()):
#     print("The first letter is lowercase. Lets make it uppercase")
#     name = name.capitalize() #Capitalize will only make the first letter uppercase
#     print(name)
#     print("Better")
# else:
#     print("Looks good to me boss")