"""""
#Adding even numbers between 1 to 100
evenTotal = 0
for number in range(2,101,2): #Use 1 as starting, if you want to calculate for odd numbers
    print(number)
    evenTotal+=number
print(evenTotal)
"""

for i in range (1,101):
   
   if i%3==0 and i%5==0:
       print("fizzbuzz")
   elif i%5==0:
        print("buzz")
   elif i%3==0:
       print("fizz")
   else:
       print(i)


