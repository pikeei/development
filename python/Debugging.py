# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("you got it")
# my_function()

# from random import randint
# dice_img = ["1","2","3","4","5","6"]
# dice_num = randint(1,7)
# print(dice_img[dice_num])

# year = int(input("Whats your year birth?: "))
# if year >1980 and year <1994:
#     print("you're millenial")
# elif year >=1994:
#     print("genz")

# pages = 0
# word_per_page = 0
# pages = int(input("number of pages: "))
# word_per_page = int(input("number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

def mutate(a_list):
    b_list=[]
    for item in a_list:
        new_item = item *2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,8,13])