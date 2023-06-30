text = "And Dhey say\nChivlary is dead\nHave a nice day"

with open('test2.txt','w') as file:
    file.write(text)

    # If you wish to add to the already created file use a instead of w. If you wish to read simply put r