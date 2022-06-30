
import math
from webbrowser import Opera


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}   
def calculator():

    first_number = float(input("Whats the first number?: "))
    calculation= False  
    while not calculation:
            
        user_pick = input("What operation do you want to use?: ")
        second_number = float(input("Whats the next number?: "))

        mathemating = Operations[user_pick]
        answer = mathemating(first_number,second_number)
        print (f"{first_number} {user_pick} {second_number} = {answer}")

        calculate_more = input(f"continue calculating with {answer}?  y for yes/n for no or do you want to make a new calculation? type CLEAR: ")
        if calculate_more=="y":
            first_number=answer
        elif calculate_more=="CLEAR":
            calculator()
        
        elif calculate_more=="n":
            calculation = True
calculator()
    