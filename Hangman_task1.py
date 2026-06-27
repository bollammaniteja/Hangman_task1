# Hangman Game
# A simple Python game where the player guesses a hidden word.

import random

# List of words
words = ["apple", "python", "school", "computer", "mobile"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 0
max_guesses = 6

print("=" * 35)
print("         HANGMAN GAME")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have", max_guesses, "wrong guesses.\n")

while wrong_guesses < max_guesses:

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Guessed Letters:", " ".join(guessed_letters))

    # Check if the player won
    if "_" not in display:
        print("\nCongratulations! You guessed the word correctly.")
        break

    # Take input
    guess = input("Enter a letter: ").lower()
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Chances:", max_guesses - wrong_guesses)

# If player loses
if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")