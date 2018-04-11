from converter import *

#Use the converter function in anyway you want
# converter(number : int)-->str
def get_check_input():
    # Getting the required number from the user
    try:
        n = int(input("Enter the digits of integer you want to convert to words:"))
        word = converter(n)
        print(word)
    #handle error if input string isnt an integer
    except ValueError as e:
        print("Please enter an integer\n")
        get_check_input()

get_check_input()