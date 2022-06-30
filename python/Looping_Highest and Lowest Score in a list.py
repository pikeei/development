
studentScores = input("What are the scores of the students?: ").split()

for i in range(0, len(studentScores)):
    studentScores[i]= int(studentScores[i])
print(studentScores)

highestScore = 0
for scores in studentScores:
    if scores > highestScore:
        highestScore=scores
print(f"the highest score is {highestScore}")


lowestScore = None 
for scores in studentScores:
    if scores < studentScores[0]:
        lowestScore=scores
print(f"the lowest score is {lowestScore}")