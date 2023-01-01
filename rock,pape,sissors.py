import random

def play():
    user = input("R:Rock"+ "\n" + "P:Paper" + "\n" +"S:Sissors" + "\n")
    computer = random.choice(["r","p","s"])
    print(f'The computer chose {computer}')  
    if user == computer:
        return "It was a tie"
    if win(user,computer):
        return "You Win" 
   
    return "You lose" 
     

def win(player, enemy):
    if(player == "r" or "R"and enemy == "s" or "S") or (player == "p" or "P" and enemy == "r" or "R" ) or (player == "s" or "S" and enemy == "p" or "P"):
        return True

print(play())


    
#     
