# set = collection which is unordered, unindexed, no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("uten") Adds to the Set
#utensils.remove("fork") Removes from the Set
#utensils.clear() Clears the Set
#utensils.update(dishes)
#dishes.update(utensils) This will update the list. In this case we are switching the Set with the other
#dinner_table = utensils.union(dishes) #In a set you need to use a union. similar to SQL

print(utensils.difference(dishes)) #What does first list stated have that second doesn't
print(dishes.difference(utensils))
print(utensils.intersection(dishes)) #Shows elements which are related

# for i in dinner_table:
#    print(i)

#for i in utensils:
#    print(i) #NOTE ,end=""; puts everything in one line

#for x in dishes:
#   print(x)

