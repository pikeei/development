import random

test_seed = int(input("Create a seed number: "))
seed = random.seed(test_seed)

randomSource = random.randint(0,1)

if (randomSource ==1):
    print("Heads")
else:
    print("Tails")
