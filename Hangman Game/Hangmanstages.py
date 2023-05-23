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
    _________
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
    _________
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
    _________
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
    _________
        """,
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |
    _________
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
    _________
        """,
        """
        --------
        |      |
        |
        |
        |
        |
    _________
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
    _________
        """)
