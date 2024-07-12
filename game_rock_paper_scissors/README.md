
### Coding the Rock, Paper, Scissors Game

Here's the code I wrote:

```python
import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors? : ").lower()

    if player == computer:
        print(f'computer: {computer}')
        print(f'player: {player}')
        print(f'Tie!')

    elif player == 'rock':
        if computer == 'paper':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You lose!')
        if computer == 'scissor':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You win!')

    elif player == 'paper':
        if computer == 'rock':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You Win!')
        if computer == 'scissor':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You lose!')

    elif player == 'scissors':
        if computer == 'paper':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You Win!')
        if computer == 'rock':
            print(f'computer: {computer}')
            print(f'player: {player}')
            print(f'You lose!')

    playAgain = input("continue (Yes/No)? : ").lower()
    if playAgain != "yes":
        break

print('Bye, see you soon!')
```

### Code Explanation

1. **Importing the Random Module:**
   ```python
   import random
   ```
   The `random` module is used to make random selections, which is crucial for simulating the computer's choice in the game.

2. **Setting Up the Game Loop:**
   ```python
   while True:
   ```
   The `while True:` loop keeps the game running until the player decides to stop.

3. **Defining Choices:**
   ```python
   choices = ['rock', 'paper', 'scissors']
   ```
   We define a list of choices that both the player and the computer can choose from.

4. **Computer's Random Choice:**
   ```python
   computer = random.choice(choices)
   ```
   The `random.choice()` function randomly selects an option from the `choices` list for the computer.

5. **Player's Choice:**
   ```python
   player = None

   while player not in choices:
       player = input("rock, paper or scissors? : ").lower()
   ```
   We initialize `player` to `None` and use a `while` loop to ensure the player enters a valid choice. The `.lower()` method converts the input to lowercase to match the choices list.

6. **Game Logic:**
   ```python
   if player == computer:
       print(f'computer: {computer}')
       print(f'player: {player}')
       print(f'Tie!')

   elif player == 'rock':
       if computer == 'paper':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You lose!')
       if computer == 'scissor':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You win!')

   elif player == 'paper':
       if computer == 'rock':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You Win!')
       if computer == 'scissor':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You lose!')

   elif player == 'scissors':
       if computer == 'paper':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You Win!')
       if computer == 'rock':
           print(f'computer: {computer}')
           print(f'player: {player}')
           print(f'You lose!')
   ```
   This section of code compares the player's choice with the computer's choice and determines the winner.

7. **Play Again Prompt:**
   ```python
   playAgain = input("continue (Yes/No)? : ").lower()
   if playAgain != "yes":
       break
   ```
   After each game, the player is asked if they want to continue. If the player enters anything other than "yes," the game loop breaks, and the game ends.

8. **Ending the Game:**
   ```python
   print('Bye, see you soon!')
   ```
   A friendly message is displayed when the game ends.