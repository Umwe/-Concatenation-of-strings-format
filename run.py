import random

def get_player():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_computer():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

def main():
    for _ in range(1000): 
        player_choice = get_player()
        computer_choice = get_computer()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)

        if winner == "draw":
            print("It's a draw! Choose again.")
        elif winner == "player":
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
