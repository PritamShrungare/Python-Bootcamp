from words import *
import random

def getRandom():
    word = random.choice(words_list)
    return word.upper()

def play(word):
    word_completion = '_' *len (word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Lets Play Hangman!')
    print(displayHangman(tries))
    print (word_completion)   
    print("\n")

    while not guessed and tries > 0:
        guess = input('enter your guess: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed the letter ',guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices=[i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if"_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You have already guessed the word ',guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a Valid Guess.')
        print(displayHangman(tries))
        print (word_completion) 
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You Win!")
    else:
        print("Sorry, you ran out tries. The word was",word)


def displayHangman(tries):
    stages = [
                """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / \\
                    -
                """,
                
                """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / 
                    -
                """,

                """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    
                    -
                """,

                """
                    --------
                    |     |
                    |     O
                    |    \\|
                    |     |
                    |    
                    -
                """,          

                """
                    --------
                    |     |
                    |     O
                    |     |
                    |     |
                    |  
                    -
                """,       

                """
                    --------
                    |     |
                    |     O
                    |     
                    |     
                    |    
                    -
                """,     

                """
                    --------
                    |     |
                    |     
                    |    
                    |     
                    |     
                    -
                """
                                              

    ]
    return stages[tries]


def main():
    word = getRandom()
    play(word)

    while input("Do you want to play again(Y/N): ").upper() == "Y":
        word = getRandom()
        play(word)

main()