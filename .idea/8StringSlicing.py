# slicing = create a substring by extracting elements from another string
#              indexing[] or slice()
#             General Formula [start:stop:step]
name = "Gianpaulo Cruz"


firstName = name[0:3] #First Index is inclusive while last is Exclusive
lastName = name[4:]
funkeyName = name[::2] #Step will skip indexes. ALSO :: would make it count all of the string index characters
reversedName = name[::-1]
print(firstName)
print(lastName)
print(funkeyName)
print(reversedName)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website[slice])
print(website2[slice])