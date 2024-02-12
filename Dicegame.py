import random
min= 1
max= 6
computerscore=0
playerscore=0
inplay=True    

def gameplay():
    global inplay
    global computerscore
    global playerscore
    while inplay:
        player= random.randint(min,max)
        computer= random.randint(min,max)
        print(f"You got {player} vs {computer}")
        if(player == computer):
            print("Tie Game")
        elif(player > computer):
            print("Player Win")
            playerscore+=1
        else:
            print("Computer Win")
            computerscore+=1
        inplay= input("Roll Again??")
        if inplay== "Exit":
            break
gameplay()
print("Game Over")
print(f"Computer Score {computerscore} vs Player Score {playerscore}")