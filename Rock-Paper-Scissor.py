import random

# All possible inputs
options = ['R', 'P', 'S']

userName = input("~~~WELCOME TO ROCK-PAPER-SCISSOR~~~\nEnter your name:\n")

# No. of rounds
rounds = int(input("Enter the number of rounds:  "))

# User's point
userPts = 0
# Computer's point
comPts = 0

tries = 1
while tries <= rounds:
    # User's input
    userInput = input("Press R -> rock\n\t  P -> paper\n\t  S -> scissor: ").upper()
    # Computer's input
    computer = random.choice(options)

    # To prevent a wrong input
    if userInput not in options:
        print("Enter a valid input!")
        continue

    elif userInput == 'R':
        if computer == 'R:
            print("\nIt's a tie!")
        elif computer == 'S':
            print(f'{userName} Wins!')
            userPts += 1
        elif computer == 'P':
            print(f'Computer wins! Hard luck {userName} :(')
            comPts += 1

    elif userInput == 'P':
        if computer == 'P':
            print("\nIt's a tie!")
        elif computer == 'R':
            print(f'{userName} Wins!')
            userPts += 1
        elif computer == 'S':
            print(f'Computer wins! Hard luck {userName} :(')
            comPts += 1

    elif userInput == 'S':
        if computer == 'S':
            print("\nIt's a tie!")
        elif computer == 'P':
            print(f'{userName} Wins!')
            userPts += 1
        elif computer == 'R':
            print(f'Computer wins! Hard luck {userName} :(')
            comPts += 1

    print(f'{rounds - tries} rounds remaining.\n'
          f"Current score is {userName} = {userPts}, Computer = {comPts}")
    tries += 1

# When the game is over.
if tries > rounds:
    print(f"\n\nGame over!\nThe final score is Computer = {comPts} & {userName} = {userPts}")
    if comPts > userPts:
        print(f"Computer wins the game, Good luck next time {userName}!!")
    elif userPts == comPts:
        print("The game ends in a draw.")
    else: print(f"Congratulations {userName}! You've won the game.")
