print("-" * 45)
print("Welcome to our game menu, choose your game!")
print("1. Tic Tac Toe")
print("2. Hangman")
option = input("Choose which game you want to play (1 - 3): ")
if option == "1":
    print("-" * 45)
    from TicTacToe import TicTacToe
elif option == "2":
    print("-" * 45)
    import HangmanGame, HangmanStages, Word_List
else:
    print("You chose a wrong number!")
