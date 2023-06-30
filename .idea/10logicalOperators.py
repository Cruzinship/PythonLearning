#logical operators (and,or,not) = used to check if two or more conditional statements is true
temp = int(input("What is the tempurture outside?: "))
#In java and would be && and or would be ||
if temp >= 0 and temp <= 30: #And operator is used for cases when you need both conditions met
    print("The temperture is good today")
    print("Go outside")
elif temp < 0 or temp > 30: #Or operator is used for the case when you need either or choice.
    print("the temperture is bad today")
    print("stay inside")
    #The not operator would be used for the case when you want conditions to have thier true or false to be flipped
    #It can kinda end up flipping things around for the norm
    #Example on implementation:
    # if temp >= 0 and temp <= 30:
    #     print("The temperture is good today")
    #     print("Go outside")