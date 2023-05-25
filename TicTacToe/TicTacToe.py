def TicTacToe():
    board = ['--', '--', '--',
             '--', '--', '--',
             '--', '--', '--']
    currentPlayer = "X"

    # PRINT BOARD
    def printBoard():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

    # TAKE INPUT
    def playerInput():
        while True:
            if currentPlayer == "X":
                inp = int(input(f"Enter a number 1-9 \033[1;34m Player (X)\033[0;0m: "))
            else:
                inp = int(input(f"Enter a number 1-9 \033[1;31m Player (0)\033[0;0m: "))
            if 1 <= inp <= 9 and board[inp - 1] == "--":
                board[inp - 1] = currentPlayer
                break
            else:
                if currentPlayer == "X":
                    print(f"That spot is already taken, please pick another spot! - \033[1;34m Player (X)\033[0;0m")
                else:
                    print(f"That spot is already taken, please pick another spot! - \033[1;31m Player (0)\033[0;0m")
                printBoard()

    # CHECK FOR WIN OR TIE
    def checkHorizontal():
        nonlocal winner
        if (board[0] == board[1] == board[2] and board[0] != "--") or (
                board[3] == board[4] == board[5] and board[3] != "--") or (
                board[6] == board[7] == board[8] and board[6] != "--"):
            winner = currentPlayer
            return True

    def checkRow():
        nonlocal winner
        if (board[0] == board[3] == board[6] and board[0] != "--") or (
                board[1] == board[4] == board[7] and board[1] != "--") or (
                board[2] == board[5] == board[8] and board[2] != "--"):
            winner = currentPlayer
            return True

    def checkDiagonal():
        nonlocal winner
        if (board[0] == board[4] == board[8] and board[0] != "--") or (
                board[2] == board[4] == board[6] and board[2] != "--"):
            winner = currentPlayer
            return True

    def checkTie():
        nonlocal gameRunning
        if "--" not in board and not checkWin():
            printBoard()
            print("It's a tie")
            gameRunning = False

    def checkWin():
        if checkDiagonal() or checkHorizontal() or checkRow():
            return True

    # SWITCH PLAYER
    def switchPlayer():
        nonlocal currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"

    # Play again
    def playAgain():
        while True:
            decision = input("Do you want to play again? (Yes/No): ")
            if decision.lower() == "yes":
                return True
            elif decision.lower() == "no":
                return False
            else:
                print("Please choose the correct answer! (Yes/No)")

    # MAIN GAME LOOP AND CHECKS
    while True:
        board = ['--', '--', '--',
                 '--', '--', '--',
                 '--', '--', '--']
        currentPlayer = "X"
        winner = None
        gameRunning = True

        # MAIN GAME LOOP AND CHECKS
        while gameRunning:
            print("Welcome to TicTacToe!")
            printBoard()
            if winner is not None:
                break
            playerInput()
            if checkWin():
                printBoard()
                print(f"The winner is {winner}")
                break
            checkTie()
            switchPlayer()

        if not playAgain():
            break
