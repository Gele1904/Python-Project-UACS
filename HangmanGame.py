import random
import HangmanStages
import Word_List


def HangMan():
    while True:
        selected_word = random.choice(Word_List.words_list)  # Randomly selects a word from the word list
        letter_guess = []
        attempts = 6  # Number of attempts the player has

        print("\033[0mWelcome to Hangman!")
        print("_ " * len(selected_word))  # Prints the word with blanks

        while True:
            print("You have", attempts, "attempts left.")
            # Ask the player to guess a letter or the full word
            guess = input("Guess a letter or the full word: ").lower()

            HangmanStages.print_hangMan(attempts)

            # Check for guessed letters
            if guess in letter_guess:
                print("You already guessed that letter. Please try again.")
                continue

            if len(guess) == 1:
                letter_guess.append(guess)
                if guess not in selected_word:
                    attempts -= 1
                    print("\033[91mWrong guess!\033[0m")
                    HangmanStages.print_hangMan(attempts)  # Print hangman figure

                word_display = ""
                for letter in selected_word:
                    if letter in letter_guess:
                        word_display += letter + " "  # Replace blanks with correct letter
                    else:
                        word_display += " _ "

                print(word_display)  # Print the word with guessed letters

                # Player wins if all letters are correct
                if "_" not in word_display:
                    print("\033[92mCongratulations,\033[0m you guessed the word correctly!")
                    break

            elif len(guess) > 1:  # Player wins if correctly guessed word
                if guess == selected_word:
                    print("\033[92mCongratulations,\033[0m you guessed the word correctly!")
                    break

                # Player loses if incorrectly guessed word
                else:
                    print("\033[91mWrong guess, you lose!\033[0m")
                    HangmanStages.print_full_hangMan()
                    print("\033[91mGame over! \033[0mYou failed to guess the word, better luck next time!")
                    print("The correct word was: " + selected_word)
                    break

            # If the player runs out of tries, the game ends
            if attempts == 0:
                print("\033[91mGame over! \033[0m You ran out of attempts.")
                print("\033[92mThe correct word was:\033[92m " + selected_word)
                break

        # Asks if you want to play again
        play_again = input("\033[94mDo you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            break
