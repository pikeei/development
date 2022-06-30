import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#list of words
list_of_words= ["cheesedog", "camel", "burger"]
chosen_word = random.choice(list_of_words)
print(chosen_word)

#creating a list of underscores that represents each letter in word
lives = 6
blanks =[]
for i in chosen_word:
    blanks+= "_"
print(blanks)

goal = False 
while not goal:
    #user guesses an i letter
    guess_letter = input("guess a letter: ").lower()
    if guess_letter in blanks:
        print(f"you already guessed this letter: {guess_letter}")
    #checking and replacement of user inputsc
    for position in range(len(chosen_word)):    
        letter = chosen_word[position]
        if letter==guess_letter:
            blanks[position] = letter
            print("correct")

            
   
    print(blanks)
    #checking if there are no longer blanks _, end the game
    if "_" not in blanks:
        goal= True
        print("you guessed the word")
    #error handler for incorrect guesses and ends the game if there are no longer lives
    if guess_letter not in chosen_word:
        print(f"you guessed {guess_letter}, but its incorrect")
        lives -=1
        if lives==0:
            goal = True
            print("you lost the game")
    print(stages[lives])



