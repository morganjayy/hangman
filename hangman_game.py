# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random,string, os

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for letter in secretWord:
        if letter not in lettersGuessed:
            return False 
        else:
            continue 
        
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guesses = ""

    for letter in secretWord:
        if letter in lettersGuessed:
            guesses += letter
        else:
            guesses += "_"

    return guesses

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabets = string.ascii_lowercase
    available_letters = ""

    for letter in alphabets:
        if letter not in lettersGuessed:
            available_letters += letter
    
    return available_letters

            
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game Hangman! \n I am thinking of a word that is ", len(secretWord), "letters long")
    
    letters_guessed_so_far = []
    number_of_trial = 8

    while number_of_trial > 0:
        print("-----------\n You have ", number_of_trial, "guesses left. \n Available letters: ",getAvailableLetters(letters_guessed_so_far))
        user_input_per_round = input("Please enter a letter: ")

        if user_input_per_round in letters_guessed_so_far:
            print("Oops! You've already guessed that letter. ",getGuessedWord(secretWord, letters_guessed_so_far))
            continue
        else:
            letters_guessed_so_far.append(user_input_per_round)

        if isWordGuessed(secretWord,letters_guessed_so_far):
            print("Good guess: ", getGuessedWord(secretWord,letters_guessed_so_far), "\n---------\n Congratulations, you won!")
            break

        elif user_input_per_round in secretWord:
            print("Good guess: ", getGuessedWord(secretWord, letters_guessed_so_far))
        
        else:
            number_of_trial -= 1
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, letters_guessed_so_far))
            if number_of_trial == 0:
                print("Sorry you ran out of guesses. The word was ", secretWord)
                break
    
hangman(chooseWord(wordlist))
