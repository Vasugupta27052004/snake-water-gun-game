import random

d={
    "r":"rock",
    "p":"paper",
    "s":"scissors"
}
options = ["rock", "paper", "scissors"]

def game():
    yourchoice = input("Enter your choice (r,p,s)")
    computerchoice = random.choice(options)
    print(f"Computer chose: {computerchoice}")
    print(f"YourChoice:{d[yourchoice]}")
    if(computerchoice==d[yourchoice]):
     print("tied")
    else:
     if(computerchoice=="rock" and yourchoice=="p"):
        print("You win")
     elif(computerchoice=="paper" and yourchoice=="s"):
        print("you win")

     elif(computerchoice=="scissors" and yourchoice=="r"):
        print("you win")
    
     elif(computerchoice=="scissors" and yourchoice=="p"):
        print("computer win")
    
     elif(computerchoice=="rock" and yourchoice=="s"):
        print("computer win")
    
     elif(computerchoice=="paper" and yourchoice=="r"):
        print("computer win")
     else:
        print("invalid input")
for i in range(6):
   
   print(f"\nRound {i+1}")
   game()
 




   
