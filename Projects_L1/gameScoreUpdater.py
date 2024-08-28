# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():
    print("You are playing the game")
    score = random.randint(1,61)
    with open("textpython.txt") as f:
        hscore = f.read()
        if hscore!="":
            hscore = int(hscore)
        else:
            hscore = 0
            
    print(f"Your score: {score}")
    if(score > hscore or hscore == ""):
        with open("textpython.txt","w") as f:
            f.write(str(score))
    return score
        
game()