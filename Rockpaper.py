import random
computerscore= 0
playerscore= 0
arr=["Rock","Paper","Scissors"]
inplay= True

def game():
    global inplay
    global computerscore
    global playerscore
    while inplay:
        player= input("Rock, Paper ,Scissors?? ").capitalize()
        computer= random.choice(arr).capitalize()
        print(f"You have Selected: {player} vs Computer has selected:{computer}")
        if (player == computer):
            print("Tie Game")
        elif (player =="Rock" ):
            if(computer== "paper"):
                print("You lose")
                computerscore+=1
            else:
                print("Computer lose")
                playerscore+=1
        elif (player== "Paper"):
            if (computer== "Rock"):
                print("Computer lose")
                playerscore+=1
            else:
                print("You lose")
                computerscore+=1
        
        elif(player == "Scissors"):
            if(computer =="Rock"):
                print("You Lose")
                computerscore+=1
            else:
                print("computer lose")
                playerscore+=1
        print(f"Computer score: {computerscore} vs player score: {playerscore}")
        inplay= input("Play again??") 
        if inplay== "exit":
            break
    print("Game Over") 
    print(f"Computer score: {computerscore} vs player score: {playerscore}")

game()
if (computerscore> playerscore):
    print("Computer Wins")
elif(computerscore< playerscore):
    print("Player Wins")
else:
    print("Its A tie")
