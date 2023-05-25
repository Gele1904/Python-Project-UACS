import random


def winner(player, computer):
    if player == computer:
        return "\033[96mIt's a tie!\033[0m"
    elif (
            (player == "Rock" and computer == "Scissors") or
            (player == "Paper" and computer == "Rock") or
            (player == "Scissors" and computer == "Paper")
    ):
        return "\033[92mPlayer wins!\033[0m"
    else:
        return "\033[91mComputer wins!\033[0m"


def play_game():
    choices = ["Rock", "Paper", "Scissors"]
    print("\033[4mWelcome to Rock Paper Scissors!\033[0m")
    while True:
        print("\033[1m\nChoose one:\033[0m")
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")
        print("0. \033[91mExit\033[0m")
        player = input("\033[4m\nEnter your choice (0-3):\033[0m ")
        if player == '0':
            print("\033[94mThank you for playing!\033[0m")
            break
        try:
            player = choices[int(player) - 1]
            computer = random.choice(choices)
            print(f"\033[1m\nPlayer chooses:\033[0m {player}")
            print(f"\033[1mComputer chooses:\033[0m {computer}")
            result = winner(player, computer)
            print(result)
        except (ValueError, IndexError):
            print("\033[91mInvalid input!\033[0m Please enter a number from 1-3 or 0 to Exit.")


play_game()
