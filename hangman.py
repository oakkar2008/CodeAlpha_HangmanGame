# Hangman Game

import random
from fruits_words import FRUITS


#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   " ),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_hangman(wrong_guesses):
    print("*" * 30)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*" * 30)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(secret_word):
    print(" ".join(secret_word))

def main():
    secret_word = random.choice(FRUITS)
    hint = ["_"] * len(secret_word)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter Your Guess Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!\nPlease Try Again!!")
            continue

        if guess in guessed_letters:
            print(f"You already guessed {guess}")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(secret_word)
            print("YOU Did it!!!!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(secret_word)
            print("YOU LOSE!!!!")
            print(f"The Answer Was {secret_word}")
            is_running = False

if __name__ == "__main__":
    main()






