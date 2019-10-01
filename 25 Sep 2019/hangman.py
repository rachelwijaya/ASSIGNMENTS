#%%
import random
chances = 10  
def random_words():
    words = ["earthquake","conversation","boyfriend","ocean","fault","vision"]
    word = random.choice(words)
    return word

def check(word,guesses,guess):
    board_display = ""
    turn = 0
    for letter in word:
        if letter in guesses:
            board_display += letter
        else:
            board_display += "_"
    if letter == guess:
        turn += 1
    if turn >= 1:
        print("Correct!")
    else:
        print("Wrong!")
        chances -= 1
    return board_display

def hangman():
    word = random_words()
    guesses = []
    guessed = False
    while not guessed:
        guess = input("Guess: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("One letter at a time, please.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter an alphabet, please.")
        elif guess in guesses:
            print("You have already guessed that.")
        elif guess in word:
            guesses.append(guess)
            answer = check(word,guesses,guess)
            if answer == word:
                guessed = True
            else:
                print(answer)
                
    print("Congratulations. The word is ",word)
    if chances >= -1:
        print("Sorry, no more chances.")

hangman()
            
        

#%%