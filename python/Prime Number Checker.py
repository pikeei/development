# import random
# import math

# def painting_calculation(height, width, coverage):
#     area = (height * width)
#     required_cans = math.ceil(area/coverage)
#     print(f"you will need {required_cans} cans to paint the area")
# height_input= int(input("what's the height?: "))
# width_input= int(input("what's the width?: "))
# coverage_input= int(input("what's the coverage?: "))

# painting_calculation(height=height_input,width=width_input,coverage=coverage_input)

def prime_checker(number):
    is_Prime = True 
    for i in range(2, number-1):
        if number%i == 0:
            is_Prime = False
    if is_Prime:
        print("its a prime number")
    else:
        print("its not a prime")

n = int(input("check this number: "))
prime_checker(number = n) 