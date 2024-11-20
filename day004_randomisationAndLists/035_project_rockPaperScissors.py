import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Computer's choice
computerChoice = random.choice(choices)

# User's choice
userChoice = input("Choose rock, paper, or scissors: ").lower()

# Game logic
if userChoice not in choices:
    print("Invalid choice! Please select rock, paper, or scissors.")
else:
    print(f"You chose: {userChoice}")
    print(f"Computer chose: {computerChoice}")

    if userChoice == computerChoice:
        print("It's a tie!")
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "scissors" and computerChoice == "paper") or \
         (userChoice == "paper" and computerChoice == "rock"):
        print("You win!")
    else:
        print("You lose!")