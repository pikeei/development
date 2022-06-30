from locale import delocalize
import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "you lose, computer has a blackjack"
    elif user_score==0:
        return "you win, you have a blackjack"
    elif user_score >21:
        return "you busted"
    elif computer_score>21:
        return "you won, computer busted"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
        
def BlackJack():
    user_cards=[]
    computer_cards=[]
    gameOver = False 


    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not gameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your current cards: {user_cards} and score: {user_score}")
        print(f"computer cards: {computer_cards[0]} and ?")     

        if user_score==0 or computer_score==0 or user_score>21:
            gameOver= True 
        else:
            user_deal = input("would you like another card?: type y/n: ")
        if user_deal=="y":
            user_cards.append(deal_card())
        else: 
            gameOver=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)
    print(f"your final hand is {user_cards} with total of {user_score}")
    print(f"computer final hand is {computer_cards} with total of {computer_score}")
    print(compare(user_score, computer_score))


while input("would you like to play a new game?: y/n")=="y":
    BlackJack()

