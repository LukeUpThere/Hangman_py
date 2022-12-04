### This is a basic hangman game.
# Luke Wilson 2022
# en_nouns.txt by 'hugsy' (https://github.com/hugsy)

import random
import os
from time import sleep

### FUNCTIONS ###

def load_word_list():
    # Opens the 'en_nouns' file and returns it as a list.
    with open('en_nouns.txt', 'r') as word_file:
        return word_file.read().split()

def failure():
    # Sets a failure condition. Prints a message and quits the program if met.
    if failure_count >= 6:
        print("Sorry, you failed. The word was '%s'." % chosen_word.title())
        sleep(3)
        return 'quit'

def success():
    # Sets a success condition. Prints a message and quits the program if met.
    if '_ ' not in displayed_word:
        print("Well done! You have correctly figured out that the word was %s"
            % chosen_word.title())
        sleep(3)
        return 'quit'

def display_word():
    # Alters displayed word to hide un-guessed characters.
    for index in range(len(chosen_word)):
        if chosen_word[index] not in choices:
            displayed_word[index] = '_ '
        else:
            displayed_word[index] = chosen_word[index]
    # Prints the displayed word in a more readable format.
    print(' '.join(displayed_word))

### HANGMAN DRAWINGS ###
hangman_drawings = ["""
     ____
     |   |
         |
         |
         |
        _|_
""","""
     ____
     |   |
     0   |
         |
         |
        _|_
""","""
     ____
     |   |
     0   |
     |   |
         |
        _|_
""","""
     ____
     |   |
     0   |
     |\  |
         |
        _|_
""","""
     ____
     |   |
     0   |
    /|\  |
         |
        _|_
""","""
     ____
     |   |
     0   |
    /|\  |
    /    |
        _|_
""","""
     ____
     |   |
     0   |
    /|\  |
    / \  |
        _|_
"""]

### MAIN PROGRAM ###

# Loads in the random word
word_list = load_word_list()
chosen_word = random.choice(word_list)

# Setting up variables
choice = ''
choices = []
failure_count = 0
displayed_word = []

# Initialises the displayed word as a list-form of the chosen word.
for letter in chosen_word:
    displayed_word.append(letter)

while choice != 'quit':
    # Clear screen. Welcome Message. Hangman drawing tied to the failure count.
    os.system('cls')
    print("Welcome to Hangman!")
    print(hangman_drawings[failure_count])
    
    display_word()
    print(chosen_word)
    print("\nGuesses: %s" % (', '.join(choices)))
    choice = success()
   
    if choice != 'quit':
        print("\nYou have %d tries remaining.\n" % (6-failure_count))
        choice = input("type 'quit' to quit.\n")
    
    # Tests if the choice was wrong or not.
    if choice != 'quit':
        if choice not in chosen_word:
            failure_count += 1
            print("\nThat's incorrect.")
            sleep(1)
        else:
            print("Correct.")
            sleep(1)
        choices.append(choice)
    
    if choice != 'quit':
        choice = failure()
    
