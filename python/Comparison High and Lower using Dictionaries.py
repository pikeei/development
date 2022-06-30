from game_data import data
import random


def format_data(data):
    """Gets data from dictionary and returns a dynamic printable statement"""
    account_name = data["name"]
    account_description = data["description"]
    account_count= data["follower_count"]
    account_country= data["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")
def check_answer(guess, a_followers, b_followers):
    """Checks if the users guesses the follower count and return if correct"""
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"
game = True
score = 0
data_b = random.choice(data)
while game:
    
    #generating data 
    data_a = data_b
    data_b = random.choice(data)

    if data_a==data_b:
        data_b=random.choice(data)
    print(f"Compare A: {format_data(data_a)}.")
    print("VS")
    print(f"Against B: {format_data(data_b)}.")


    guess = input("Who has more followers? A/B: ").lower()
    a_follower_count = data_a["follower_count"]
    b_follower_count = data_b["follower_count"]

    is_correct = check_answer(guess=guess,a_followers=a_follower_count,b_followers=b_follower_count)

    if is_correct:
        score+=1
        print(f"you guessed it right, current score is {score}")
        
    else:
        print(f"wrong guess, final score is {score}")
        game = False