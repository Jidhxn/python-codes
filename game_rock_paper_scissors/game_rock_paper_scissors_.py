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

print('Bye, see yo soon!') 


