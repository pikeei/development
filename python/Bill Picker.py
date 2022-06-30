import random
from unicodedata import name
test_seed = int(input("Enter a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me some names separated by comma e.g a,b,c")
names = namesAsCSV.split(",")

randomIndex = random.randint(0, len(names)-1)
print(randomIndex)
chosenOne = names[randomIndex]

print(f"the one who will pay the bill is {chosenOne}")