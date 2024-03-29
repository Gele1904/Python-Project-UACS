import HangmanGame
from TicTacToe import TicTacToe
import RockPaperScissors
import Instructions


def chooseAgain():
    while True:
        decision = input("Do you want to choose again? (Yes/No): ")
        if decision.lower() == "yes":
            return True
        elif decision.lower() == "no":
            return False
        else:
            print("Please choose the correct answer! (Yes/No)")


while True:
    print("\033[0mWelcome to our game menu, choose your game!")
    print("-" * 45)
    print("1. Tic Tac Toe")
    print("2. Hangman")
    print("3. Rock Paper Scissors")
    print("\033[31m0. Exit\033[0m")
    print("-" * 45)
    print("Instructions")
    print("4. Tic Tac Toe Instructions")
    print("5. Hangman Instructions")
    print("6. Rock Paper Scissors Instructions")
    print(" ")
    option = int(input("Choose one of the following options (1 - 6) (0 For Exit): "))
    if option == 1:
        print("-" * 45)
        TicTacToe.TicTacToe()
    elif option == 2:
        print("-" * 45)
        HangmanGame.HangMan()
    elif option == 3:
        RockPaperScissors.Rock_Paper_Scissors()
    elif option == 4:
        Instructions.TicTacToeInstructions()
    elif option == 5:
        Instructions.HangManInstructions()
    elif option == 6:
        Instructions.RockPaperScissorsInstructions()
    elif option == 0:
        break
    else:
        print("\033[31mWrong option (Select 1 - 6)!")

        if not chooseAgain():
            break
