### Code Explanation

#### Starting a New Game

```python
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
```

- **Function Definition:** `def newGame()` starts the game.
- **Initialization:** `questionNumber`, `guesses`, and `correctGuesses` are initialized to keep track of the game state.
- **Loop Through Questions:** The `for key in questions` loop iterates through each question.
- **Display Question and Options:** The question and its corresponding options are printed.
- **Get Player’s Guess:** The player's guess is taken as input and appended to the `guesses` list.
- **Check Answer:** The `checkAnswer` function is called to verify the player's guess and update the `correctGuesses` count.
- **Next Question:** The `questionNumber` is incremented for the next iteration.
- **Display Score:** After all questions are answered, `displayScore` is called to show the results.

#### Checking Answers

```python
def checkAnswer(answer, guess):
    if answer[:1] == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
```

- **Function Definition:** `def checkAnswer(answer, guess)` checks if the player's guess is correct.
- **Correct Guess:** If the first character of the answer matches the guess, "CORRECT!" is printed and 1 is returned.
- **Incorrect Guess:** Otherwise, "WRONG!" is printed and 0 is returned.

#### Displaying the Score

```python
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
```

- **Function Definition:** `def displayScore(correctGuesses, guesses)` shows the final results.
- **Print Results Header:** Prints a header for the results section.
- **Print Correct Answers:** Loops through `questions` to print the correct answers.
- **Print Player’s Guesses:** Loops through `guesses` to print the player's guesses.
- **Final Score:** Prints the player's final score.

#### Play Again Function

```python
def playAgain():
    response = input("Do you want to play again ? [Yes/No] : ").lower()
    if response == "yes" or response == "y":
        return True
    else:
        return False
```

- **Function Definition:** `def playAgain()` asks the player if they want to play again.
- **Check Response:** If the response is "yes" or "y", returns `True` to restart the game; otherwise, returns `False`.

#### Questions and Options

```python
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
```

- **Questions Dictionary:** `questions` contains the quiz questions and their correct answers.
- **Options List:** `options` contains the possible answers for each question.

#### Main Game Loop

```python
newGame()

while playAgain():
    newGame()

print("Bye, see you soon :)")
```

- **Start New Game:** `newGame()` is called to start the first game.
- **Play Again Loop:** The game continues to restart as long as `playAgain()` returns `True`.
- **End Message:** Prints a friendly goodbye message when the player chooses not to play again.
