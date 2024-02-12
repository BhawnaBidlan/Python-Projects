import time
def countdown(t):
    while t:
        min = t // 60
        sec = t % 60
        output = "Your Time left is {:02d}:{:02d}".format(min, sec)
        print(output)
        time.sleep(1)
        t-=1
    print("Time is up!!")
    start()

def start():
    t=input("Enter the  number of second:")
    if t.isnumeric():
        countdown(int(t))
    else:
        print("Was not a number")
        start()
start()
 
