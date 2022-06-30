
studentHeights = input("Input a height of students ").split()
for n in range(0,len(studentHeights)):
    studentHeights[n]=int(studentHeights[n])
print(studentHeights)

totalHeight = 0
for height in studentHeights:
    totalHeight+=height
print(totalHeight)

numberOfStudent = 0

for number in studentHeights:
    numberOfStudent+=1
print(numberOfStudent)

avg = totalHeight/numberOfStudent
print(avg)