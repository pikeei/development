import random
test_seed = int(input("Create a seed number: "))
seed = random.seed(test_seed)

playerChose = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors.: "))

aiChoose = random.randint(0,2)
print(f"The computer chosen {aiChoose}")

if playerChose==aiChoose:
    print("Draw")
elif playerChose== 0 and aiChoose==2:
    print("player wins")
elif playerChose==2 and aiChoose==1:
    print("Player wins")
elif playerChose==1 and aiChoose0:
    print("Player wins")
elif playerChose >=3 or playerChose <0:
    print("invalid input    ")
else:
    print("you lose")