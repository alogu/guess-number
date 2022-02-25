from math import inf
import random
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

def Guess(num):
    guessed_num = 0
    actual_num = random.randint(1, num)

    while guessed_num != actual_num:
        try:
            guessed_num = int(input("Please enter a number between 1 and {num}: "))
            assert isinstance(guessed_num, int)

        except :
            print('Invalid input! Please type integers only!')

        else:
            if guessed_num < actual_num:
                print("Your guess is lower than the actual number\nTry Again!\n")
            elif guessed_num > actual_num:
                print("Your guess is larger than the actual number.\nTry Again!\n")
            else:
                print("Congratulations! You have guessed my number correctly!\n")

def Guess_Computer():
    computer_num = 0
    lower_bound = 1
    upper_bound = 100

    user_feedback = ''
    actual_num = int(input('Please enter a number between 1 and 100 for the computer to guess: \n'))

    while user_feedback != 'c':
        computer_num = random.randint(lower_bound, upper_bound)
        user_feedback = input(f'The current computer guess is {computer_num}, is this high(h), low(l), or correct(c)?: ').strip().lower()

        if user_feedback == 'h':
            upper_bound = computer_num - 1
        elif user_feedback == 'l':
            lower_bound = computer_num + 1
        elif user_feedback == 'c':
            print('Congratulations! You\'ve guessed the correct number!')
        else:
            print('Invalid user input, please try again.')
        
Guess_Computer()
