import random

# The range of number in which you want to guess from.
number_range = input("Enter the range of number you want to guess from (0 to _): ")
if number_range.isdigit():
    number_range = int(number_range)
    if number_range <= 0:
        print("Enter a number greater than 0.")
        quit()
else:
    print("Enter a valid input.")
    quit()

random_number = random.randint(0, number_range)

# The number of guesses the user wants to have
guesses = input("Enter the number of rounds: ")
if guesses.isdigit():
    guesses = int(guesses)
    if guesses <= 0:
        print("Enter a number greater than 0.")
        quit()
else:
    print("Enter a valid input.")
    quit()
start = 1

# Handling guesses of the user
while start <= guesses :
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print(f"Yay! you got it in {start} guesses.")
            break
        elif user_guess < random_number:
            print("Guess a greater number.")
        else:
            print("Guess a smaller number.")
        print(f"You have {guesses - start} rounds remaining")
    else:
        print("Enter a number.")
        continue
    start += 1

# Game Over
if start > guesses:
    print("Game over!")

