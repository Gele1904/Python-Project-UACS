import random


def hangMan():
    words_list = [
        "elephant", "computer", "butterfly", "sunshine", "rain", "rainbow", "chocolate", "baseball", "adventure",
        "pizza", "guitar", "summer", "happiness", "ocean", "jungle", "friendship", "mystery", "diamond",
        "fireworks", "vacation", "apple", "banana", "cherry", "date", "fig", "grape"
    ]

    while True:
        selected_word = random.choice(words_list)  # Randomly selects a word from the word list
        letter_guess = []  # Store the letters guessed by the player
        attempts = 6  # Number of attempts the player has

        print("Welcome to Hangman!")
        print("_ " * len(selected_word))  # Prints the word with blanks

        while True:
            print("You have", attempts, "attempts left.")
            # Ask the player to guess a letter or the full word
            guess = input("Guess a letter or the full word: ").lower()

            # Check for guessed letters
            if guess in letter_guess:
                print("You already guessed that letter. Please try again.")
                continue

            if len(guess) == 1:  # If the guess is a single letter
                letter_guess.append(guess)  # Add the guessed letter to guessed letters
                if guess not in selected_word:  # If the guessed letter is not in the chosen word
                    attempts -= 1  # Decrease the number of attempt if guess is wrong
                    print("Wrong guess!")
                    print_hangMan(attempts)  # Print hangman figure

                word_display = ""
                for letter in selected_word:
                    if letter in letter_guess:
                        word_display += letter + " "  # Replace blanks with correct letter
                    else:
                        word_display += "_ "

                print(word_display)  # Print the word with guessed letters

                # Player wins if all letters are correct
                if "_" not in word_display:
                    print("Congratulations, you guessed the word correctly!")
                    break

            elif len(guess) > 1:  # If the guess is the full word
                if guess == selected_word:  # If the guessed word matches the selected word
                    print("Congratulations, you guessed the word correctly!")
                    break

                # Player loses if the guessed word is incorrect
                else:
                    print("Wrong guess, you lose!")
                    print_full_hangMan()
                    break

            # If the player runs out of tries, ends the game
            if attempts == 0:
                print("Game over! You ran out of attempts.")
                print("The correct word was:", selected_word)
                break

        # Asks if you want to play again
        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            break


# Prints the hangman figure corresponding with the number of attempts left
def print_hangMan(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    print(stages[attempts])


# Prints the full hangman if the word is guessed incorrectly
def print_full_hangMan():
    print("""
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """)


hangMan()
