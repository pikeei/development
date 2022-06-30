
import random
import string 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Number Generator")
numberOfLetters = int(input("How many letters would you like to be in your password?: "))
numberOfNumbers = int(input("How many numbers would you like to be in your password?: "))
numberOfSymbols = int(input("How many symbols would you like to be in your password?: "))

password = []

for character in range(0,numberOfLetters):
   password +=  random.choice(letters)

for number in range(0,numberOfNumbers):
    password+=random.choice(numbers)
for symbol in range(0,numberOfSymbols):
    password+=random.choice(symbols)
   
print(password)   
random.shuffle(password)

passwordString = ""
for i in password:
    passwordString+=i
print(f"your randomized password is: {passwordString}")
      
