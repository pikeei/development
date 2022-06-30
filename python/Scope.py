import random
#my first attempt
# numbers = []
# for i in range(1,100+1):
#     i+i
#     numbers.append(i)
# random_number = random.choice(numbers)

# easy = 10
# hard = 5
# life = None
# difficulty = input("choose a difficulty: 'easy' or 'hard' ")
# if difficulty=="easy":
#     life=easy
# elif difficulty=="hard":
#     life=hard
# else:
#     print("invalid input")

# game_over= False
# while not game_over:
#     guess = int(input("guess the number: "))
#     print(random_number)
#     if guess==random_number:
#         game_over=True
#         print("you guessed it")
#     elif guess>random_number:
#         life-=1
#         print(f"too high, your current life is {life}")
        
#     elif guess <random_number:
#         life-=1
#         print(f"too low, your current life is {life}")
#     if life==0:
#         game_over=True
EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    difficulty = input("choose a difficulty: 'easy' or 'hard' ")
    if difficulty=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def check_answer(guess, answer,life):
    if guess>answer:
        print("too high")
        return life-1
       
    elif guess <answer:
        print("too low")
        return life-1
        
    elif guess==answer:
        print(f"you guessed it correctly which is {answer}")
        
def game():
    answer = random.randint(1,100)
    print(answer)
    life = set_difficulty() 
    guess = 0
    while guess!=answer:
        print(f"You have {life} attempts")
        guess= int(input("guess the number: "))
        life = check_answer(guess,answer,life)
        if life==0:
            print("you lost")
            
            
            
while input("would you like to play a new game of guess? y/n: ")=="y":
    game()
            