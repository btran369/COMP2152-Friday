import random
choices = ["Rock", "Paper", "Scissors"]


def main():
    try:
        playerChoice = input("Enter your choice: Rock, Paper or Scissors: ").capitalize()
        print(playerChoice)
        if playerChoice not in choices:
            raise ValueError("Invalid choice, try again")
        compChoice = choices[random.randint(0,2)]
        print(compChoice)
        print((playerChoice == compChoice))
        print(f"Player choice: {playerChoice}")
        print(f"Computer choice: {compChoice}")
        if playerChoice == compChoice:
            print("It's a tie!")
        checkTuple = (playerChoice,compChoice)
        if checkTuple == ("Rock", "Paper") or checkTuple == ("Paper", "Scissors") or checkTuple == ("Scissors", "Rock"):
            print("Computer wins!")
        else:
            print("Player wins!")
    except:
        print("Ooops!")

if __name__ == "__main__":
    main()