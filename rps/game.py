import random

you_wins = 0
computer_wins = 0
tie_wins = 0

# storing the options in an index
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if you_wins == "q":
        break

    if you_wins not in options:
        continue
    
    # counting in an array rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0,2)
    # get the computer to randomize choice between rock paper scissor
    computer_pick = options[random_number]
    print("Computer has chosen", computer_pick + ".")

    # treated like an and or statement to compare my choice to computers random choice
    # My possibilities of winning
    if user_input == "rock" and computer_pick == "scissors":
        print("You won this time!")
        you_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You have won this time!")
        you_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won this time!")
        you_wins += 1

        # our possibilities of draws
    elif you_wins == "scissors" and computer_pick == "scissors":
        print("No One wins!")
        tie_wins +=1

    elif you_wins == "rock" and computer_pick == "rock":
        print("No One wins!")
        tie_wins +=1

    elif you_wins == "paper" and computer_pick == "paper":
        print("No One wins!")
        tie_wins +=1

    else:
        print("You lose this one!")
        computer_wins += 1

# shows both win totals
print("You won", you_wins, "times.")
print("Computer won", computer_wins, "times.")

# only shows if the amount of ties is greater or equal to 1
if tie_wins >= 1:
    print("You and the computer tied", tie_wins, "times.")

# ending program
print("See yu")
