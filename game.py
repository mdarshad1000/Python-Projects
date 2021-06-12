#SNAKE WATER GUN
import random
options = ["s", "w", "g"]
computer = random.choice(options)

a = "User wins!"
b = "Computer wins!"
point_user = 1
point_comp = 1
i = 1
while(i <= 10):

    user = input("Enter 'g' for gun, 's for snake', 'w' for water :\n")
    if (computer == 'g' and user == 'g') or (computer == 'w' and user == 'w') or (computer == 's' and user == 's'):
        print("It's a tie!")
    elif computer == 'g' and user == 'w':
        print(a,f"\nUser's point is {point_user}")
        point_user = point_user + 1
    elif computer == 's' and user == 'g':
        print(a,f"\nUser's point is {point_user}")
        point_user = point_user + 1
    elif computer == 'w' and user == 's':
        print(a,f"\nUser's point is {point_user}")
        point_user = point_user + 1
    elif computer == 'g' and user == 's':
        print(b,f"\nComputer's point is {point_comp}")
        point_comp = point_comp + 1
    elif computer == 's' and user == 'w':
        print(b,f"\nComputer's point is {point_comp}")
        point_comp = point_comp + 1
    elif computer == 'w' and user == 'g':
        print(b,f"\nComputer's point is {point_comp}")
        point_comp = point_comp + 1
    else:
        print("Enter valid input!")
        break
    print(f"{10 - i} rounds remaining\n"
          f"Current score is U = {point_user-1}, C = {point_comp-1}")
    i = i + 1

print(f"The final score is Computer = {point_comp-1},User = {point_user-1}")
if point_comp - 1 > point_user - 1:
    print("Computer wins the game!")
elif point_user - 1 == point_comp - 1:
    print("The game ends in a draw")
else: print("User wins the game")

if i > 10:
    print(f"Game over!")


