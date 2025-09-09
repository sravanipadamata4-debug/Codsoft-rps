import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    player = input("Choose Rock, Paper, or Scissors (or 'quit' to exit): ").capitalize()
    if player == "Quit":
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:  # computer == "Scissors"
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
        else:  # computer == "Rock"
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
        else:  # computer == "Paper"
            print("You win!")

    print()  # Blank line for readability