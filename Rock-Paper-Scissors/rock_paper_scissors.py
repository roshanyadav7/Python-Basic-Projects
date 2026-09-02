import random

def get_player_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        player = input("Choose rock, paper, or scissors: ").lower().strip()
        if player in choices:
            return player

        print("Invalid choice! Please try again.")


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player, computer):
    if player == computer:
        return "tie"
    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    
    return "computer"

def display_score(player_score, computer_score):
    print("\n" + "-" * 30)
    print("SCORE")
    print("You     :", player_score)
    print("Computer:", computer_score)
    print("-" * 30)

def play_game():
    player_score = 0
    computer_score = 0
    round_number = 1
    print("\n" + "=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("            BEST OF 5")
    print("=" * 40)
    while player_score < 3 and computer_score < 3:
        print(f"\n--- Round {round_number} ---")
        player = get_player_choice()
        computer = get_computer_choice()
        print("You chose     :", player)
        print("Computer chose:", computer)
        winner = determine_winner(player, computer)
        if winner == "tie":
            print("It's a tie! 🤝")
        elif winner == "player":
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1
        display_score(player_score, computer_score)
        round_number += 1
    print("\n" + "=" * 40)
    if player_score == 3:
        print("🎉 CONGRATULATIONS! YOU WIN THE GAME!")
    else:
        print("💻 COMPUTER WINS THE GAME!")
    print(f"Final Score: You {player_score} - {computer_score} Computer")
    print("=" * 40)
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if again != "yes":
        print("\nThanks for playing! 👋")
        break