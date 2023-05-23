def playAgain():
    while True:
        decision = input("Do you want to play again? (Yes/No): ")
        if decision.lower() == "yes":
            return True
        elif decision.lower() == "no":
            return False
        else:
            print("Please choose the correct answer! (Yes/No)")


while True:
    print("-" * 45)
    print("\033[0mWelcome to our game menu, choose your game!")
    print("1. Tic Tac Toe")
    print("2. Hangman")
    print("3. -----------")
    print("4. Exit")
    option = input("Choose which game you want to play (1 - 3) (4 For Exit): ")
    if option == "1":
        print("-" * 45)
        from TicTacToe import TicTacToe
    elif option == "2":
        print("-" * 45)
        import HangmanGame, HangmanStages, Word_List
    elif option == "3":
        print("The game is still in development!")
    elif option == "4":
        break
    else:
        print("You chose a wrong number!")

        if not playAgain():
            break
