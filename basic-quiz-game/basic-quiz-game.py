def newGame():

    questionNumber = 1
    guesses = []
    correctGuesses = 0

    for key in questions:
        print("------------------------------------------------")
        print(key)
        for i in options[questionNumber-1]:
            print(i)
        guess = input("Your answer (a,b,c, or d) : ").lower()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        questionNumber += 1

    displayScore(correctGuesses, guesses)

#------------------------------------------------------------------------
def checkAnswer(answer, guess):
    if answer[:1] == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#------------------------------------------------------------------------
def displayScore(correctGuesses, guesses):
    print("------------------------------------------------")
    print("RESULTS")
    print("------------------------------------------------")
    print("Answers : ", end=" ")
    for i in questions:
        print(questions.get(i)[:1], end=" ")
    print()

    print("Guesses : ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    print(f'Your final score is {correctGuesses}.')

#-----------------------------------------------------------------------

def playAgain():
    response = input("Do you want to play again ? [Yes/No] : ").lower()
    if response == "yes" or response == "y":
        return True
    else:
        return False

#------------------------------------------------------------------------

questions = {
    "What is the capital of France?: ": "c) Paris",
    "Who wrote the play 'Romeo and Juliet'?: ": "b) William Shakespeare",
    "What is the largest planet in our solar system?: ": "c) Jupiter",
    "Which element has the chemical symbol 'O'?: ": "b) Oxygen",
    "Who is known as the 'Father of Computers'?: ": "b) Charles Babbage"
}


options = [
    ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
    ["a) William Wordsworth", "b) William Shakespeare", "c) Charles Dickens", "d) George Orwell"],
    ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) Gold", "b) Oxygen", "c) Silver", "d) Osmium"],
    ["a) Alan Turing", "b) Charles Babbage", "c) Thomas Edison", "d) Alexander Graham Bell"],
]


newGame()

while playAgain():
    newGame()

print("Bye, see you soon :)")



