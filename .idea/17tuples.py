# tuples = collections which is order and unchangeable
# tuples are simply amazing and they dont exist in Java, most similar to a normal ArrayList in java
#          used to group together related data
student = ("Gianpaulo",18,"male")  #This order will not change

print(student.count("Gianpaulo")) # This counts how many Gianpaulos there will be
print(student.index("male")) # This will retrieve the index of the element selected

for i in student: # Prints all from the list using the for loop
    print(i)

if ("Gianpaulo" and "male") in student: # If Gianpaulo and Male are within student then print the following
    print("Gianpaulo is here")