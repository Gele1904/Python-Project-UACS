import random


# Determines the winner of the round
def winner(player, computer):
    if player == computer:
        return "tie"
    elif (
            (player == "Rock" and computer == "Scissors") or
            (player == "Paper" and computer == "Rock") or
            (player == "Scissors" and computer == "Paper")
    ):
        return "player"
    else:
        return "computer"


def game():
    choices = ["Rock", "Paper", "Scissors"]
    print("\033[4mWelcome to Rock Paper Scissors!\033[0m")
    rounds_to_win = 2
    player_wins = 0
    computer_wins = 0

    while player_wins < rounds_to_win and computer_wins < rounds_to_win:
        # Displays available choices for the player to input
        print("\033[1m\nChoose one:\033[0m")
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")
        print("0. \033[91mExit\033[0m")
        player = input("\033[4m\nEnter your choice (0-3):\033[0m ")

        # Exits the game if the player chooses number 4
        if player == '0':
            print("\033[94mThank you for playing!\033[0m")
            break

        # Converts player input to the corresponding choice and makes a random selection for the computer
        try:
            player = choices[int(player) - 1]
            computer = random.choice(choices)
            print(f"\033[1m\nPlayer chooses:\033[0m {player}")
            print(f"\033[1mComputer chooses:\033[0m {computer}")
            result = winner(player, computer)

            # Increments the player/computer's score and displays the round result if player/computer wins
            if result == "player":
                print(f"\033[96mRound {player_wins + computer_wins + 1}:\033[0m \033[95mPlayer\033[0m wins the round!")
                player_wins += 1
            elif result == "computer":
                print(
                    f"\033[96mRound {player_wins + computer_wins + 1}:\033[0m \033[93mComputer\033[0m wins the round!")
                computer_wins += 1
            else:
                # Round is displayed as a tie if it's a tie
                print(f"\033[96mRound {player_wins + computer_wins + 1}:\033[0m \033[96mIt's a tie!\033[0m")

            # Shows the current score
            print(f"\033[96mScore:\033[0m Player {player_wins} - {computer_wins} Computer")

        except (ValueError, IndexError):
            # Handles invalid inputs
            print("\033[91mInvalid input!\033[0m Please enter a number from 1-3 or 0 to Exit.")

    # Displays the final result of the game based on the score
    if player_wins > computer_wins:
        print("\033[92mPlayer wins the game!\033[0m")
    elif player_wins < computer_wins:
        print("\033[91mComputer wins the game!\033[0m")
    else:
        print("\033[96mIt's a tie game!\033[0m")


# Play again
while True:
    game()
    play_again = input("\033[94m\nDo you want to play again? (Yes/No):\033[0m ").lower()
    while play_again not in ["yes", "no"]:
        print("Please choose the correct answer! (Yes/No)")
        play_again = input("\033[94mDo you want to play again? (Yes/No):\033[0m ").lower()
    if play_again != "yes":
        break
