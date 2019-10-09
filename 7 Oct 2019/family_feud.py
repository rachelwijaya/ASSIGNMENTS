#Family Feud Game
P1score = 0
P2score = 0
P1 = ""
P2 = ""
def player_names(P1,P2):
    P1 = input("Enter your name Player 1: ")
    P2 = input("Enter your name Player 2: ")
    print("Welcome to Family Feud, " + P1 + " and " + P2)
    return P1, P2

def family_feud(P1,P2):
    questions = ["Name something you keep in your wallet: ", "Name a kind of cheese: ", "Name a lollipop flavor: ",
                 "Name something you find in a park", "Name a kind of cake: "]  
    class QnA():
        def Q1():
            global P1score
            global P2score
            print(questions[0])
            answers = {"money": 84, "driver's license": 57, "pictures":42,"credit cards": 41,"identification":56}
            anscopy = answers.copy()
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P1score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P2score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
        def Q2():
            global P1score
            global P2score
            print(questions[1])
            answers = {"cheddar": 92, "swiss": 34, "american": 53, "blue": 45, "longhorn": 14}
            anscopy = answers.copy()
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P1score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P2score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
        def Q3():
            global P1score
            global P2score
            print(questions[2])
            answers = {"cherry": 66, "strawberry": 74, "grape": 45, "orange": 59, "lemon": 25}
            anscopy = answers.copy()
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P1score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P2score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
        def Q4():
            global P1score
            global P2score
            print(questions[3])
            answers = {"benches": 65, "trees": 63, "birds": 48, "grass": 33, "swings": 29}
            anscopy = answers.copy()
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P1score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P2score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
        def Q5():
            global P1score
            global P2score
            print(questions[4])
            answers = {"chocolate": 40, "angel food": 55, "pound": 60, "birthday": 78, "cheesecake": 63}
            anscopy = answers.copy()
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P1score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
            guess = input("Enter your guess: ")
            guess = guess.lower()
            if guess in anscopy:
                print("You've guessed right!")
                P2score += answers[guess]
                anscopy.pop(guess)
            else:
                print("Sorry it isn't there.")
    for i in range(len(questions)):
        if i == 0:
            QnA.Q1()
        elif i == 1:
            QnA.Q2()
        elif i == 2:
            QnA.Q3()
        elif i == 3:
            QnA.Q4()
        elif i == 4:
            QnA.Q5()
    if P1score >= 200 and P1score > P2score:
        print("The winner is " + str(P1) + " with " + str(P1score) + " points.")
    elif P2score >= 200 and P2score > P1score:
        print("The winner is " + str(P2) + " with " + str(P2score) + " points.")
    else:
        print("There is no winner. Game Over.")
P1, P2 = player_names(P1,P2)
family_feud(P1,P2)
#%%