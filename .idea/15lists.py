# list = used to stroe multiple items in a single variable
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
food[0] = "sushi"
print(food[0])

print("----------------------------------------")

food.append("ice cream") #Adds to the list to the end of the list
food.remove("hotdog") #Removes matcthing data
food.pop() #Removes last element
food.insert(0,"cake") #Adds new element to the list where you want
food.sort() #Sorts our list Alphaetically
#food.clear() This clears our list
for i in food:
    print(i)