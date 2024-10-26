# Game with mercedes,addison,sierra,cadence :)
# Hangman!!

import random
def hangman():
    # ADDISON  make something that meausure how far you are from losing the game.(hangman)
    # ADDISON  assign how to input random word for the user to guess.

    word_list = ["bannana", "cake", "computer", "coconut", "apple", "headphones"]
    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts try do guess one of the words good luck!!.")
    #CADENCE: 3. create something that helps deteremine if the letter the user put is part of the random word.
    while attempts > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        #MERCEDES: 4. something that allows the user to input a letter that determines if the letter is part of the random generated word

        if guess in guessed_letters:
            print("You've already guessed that letter WHOOPS!.")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            guessed_letters.add(guess)
        else:
           #SIERRA: 6. use a decision making process to accept only alphabets as names
           #SIERRA: 5. define another loop that makes it play again
            print(f"Sorry, '{guess}' is not in the word try again!.")
            attempts -= 1
            guessed_letters.add(guess)

        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nOut of attempts! The word was:", word)

# Run the game
hangman()
