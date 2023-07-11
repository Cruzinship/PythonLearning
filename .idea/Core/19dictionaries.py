# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hasing, allow us to access a value quickly
# This dictionary works like a Map in Java
capitals = {'USA': 'Washington DC',
            'India' : 'New Dehli',
            'China' : 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany' : 'Berlin'})
capitals.update({'USA':'Las Vegas'})

print(capitals["Russia"]) #Just like when you search for an index, for map you type in the KEY into the brackets
print(capitals.get('Germany')) #Another way to locate the value of the keyname
print(capitals.pop('China')) #Gets rid of either the latest added or whatver you point to
print(capitals.keys()) #Grabs all KEYS
print(capitals.values()) #Grabs all values
print(capitals.items()) #prints all in thier own seperate spaces
capitals.clear() #whipes the dictionary values

for key,value in capitals.items():
    print(key, value) #Will iterate once per each key value
