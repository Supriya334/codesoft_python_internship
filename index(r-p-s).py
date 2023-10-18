import random
options=["rock","paper","scissors"]
my_score=0
com_score=0
running= True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter a choice(  rock,    paper,  scissors  ): ")
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if (player==computer):
        print("Tie:ribbon:")
    elif(player==   "rock"   and computer==   "scissors"   ):
        my_score+=1
        print("You Win! :sunglasses:")
    elif(player==   "paper"    and computer ==  "rock"      ):
        my_score+=1
        print("You Win!:sunglasses: ")
    elif(player==   "scissors" and computer== "paper"    ):
        my_score+=1
        print("You Win! :sunglasses:")
    else:
        com_score+=1
    print("Computer Win! :computer:","My_Score",my_score,"Computer _Score",com_score)
    play_again= input("play again?(yes/no):").lower()
    if not play_again=="yes":
        running=False
print("Thanks For Playing:heart:")