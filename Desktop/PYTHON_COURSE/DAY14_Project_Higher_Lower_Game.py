import random
import os
from Higher_Lower_Game_Data import data
from DAY14_Higher_Lower_Game_Art import logo,vs
def format_data(account):
    """takes the account data and return the printable format """
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return (f"{account_name},a {account_descr},from {account_country}")



def checkAnswer(guess,a_followers,b_followers):
    """Take the user guess & follower counts & returns if they got it right"""
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
    
    
print(logo)
score=0
game_should_Continue=True
account_b=random.choice(data)
#make game repetable
while game_should_Continue==True:
    #generate an account from the game data
    #making account at  position B  become the next account at position A
    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")
    #ask the user for guess
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    #Get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=checkAnswer(guess,a_follower_count,b_follower_count)
    #Clear the screen
    clear=lambda:os.system('cls')
    clear()
    print(logo)
    #check if user correct
    #give user feedback on their guess 
    if is_correct:
        score+=1
        print(f"you are right! Current score:{score}")
    else:
        game_should_Continue=False
        print(f"you are wrong Final Score:{score}")
        
    #score keeping

