def new_game():

    guesses = []
    correctGuesses = 0
    questionNum = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[questionNum-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        questionNum += 1

    displayScore(correctGuesses, guesses)


def checkAnswer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0

def displayScore(correctGuesses, guesses):
    print("-----------------------")
    print("RESULT")
    print("-----------------------")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correctGuesses/len(questions)*100)
    print("Your score is: " + str(score)+"%")

def playAgain():
    response = str(input("Do you want to play again? (yes or no?): "))
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Why do I code? ": "A",
    "When is my birthday? ": "B",
    "Who is my favorite super hero? " : "C",
    "The earth is round ": "A",
    "What color is my shit? ": "D",
    "Which of my birds is my favorite? ": "B",
    "What's my favorite food? " :"D",
    "What's my favorite drink? " :"B",
    "What highscool did I graduate from? ": "C",
    "Whats my Tennis/Sneaker shoe size? ": "A"


}

options = [["A. Money", "B. Birds" , "C. Always loved the idea of creating things myself", "D. Mark Zuckerburg"],
           ["A. July 27", "B. July 26", "C. July 16", "D. June 26"],
           ["A. Superman", "B. Batman", "C. Spiderman", "D. Walter White"],
           ["A. True","B. False", "C. sometimes", "D. Whats an Earth?"],
           ["A. Red", "B. Black", "C. Yellow", "D. Brown"],
           ["A. Green monster", "B. Kuku Nut", "C. Sparrow", "D. Teal monster"],
           ["A. Lomo Saltado", "B. Ceviche", "C. Causa", "D. Lasangna"],
           ["A. Water", "B. Maracuyá", "C. Chicha Morada", "D. Inca cola"],
           ["A. John F Kennedy", "B. Rockville", "C. Richard Montgomery", "D. Walter Johnson"],
           ["A. 13", "B. 12", "C. 12 1/2", "D. 11"]]

new_game()

while playAgain():
    new_game()

print("Byeeeeee:")