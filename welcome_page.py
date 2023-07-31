import os
import random
from guessing_game import *

def intro_game():
    text="Here are your options:\n'p' Display options\n'r' Print the rules\n'c' Start the game\n'q' Quit the program"
    text="\n=================\n"+text+"\n=================\n"
    print(text)
    
    while True:
        option=str(input())
        rules="""-The game consists of spinning a wheel with numbers ranging from 0 to 10.\n-Enter your name\n-Pick a number from 0 to 10\n-Spin the wheel\n-If the number you picked is the same as the random number we got from spinning the wheel, the number will be converted to points and added to your score.\n-If the number you picked is different from the random number we got from spinning the wheel, a point will be deducted from your score.\n-You will have 10 spins\n-At the end of the game, if your score greater than 0, you won.\n-If the score is less than or equal to 0, you lose"""
        rules="\n=================\n"+rules+"\n=================\n"

        if option== 'p':
            print("Option:",option)
            text="Here are your options:\n'p' Display options\n'r' Print the rules\n'c' Start the game\n'q' Quit the program"
            text="\n=================\n"+text+"\n=================\n"
            print(text)

        elif option== 'r':
            print("Option:",option)
            print(rules)

        elif option== 'c':
            print("Option:",option)
            game()

        elif option== 'q':
            print("Option:",option)
            break

        else:
            print("What you have entered is not option")

        print("\nPlease press q to quit the program or p to display the options")


if __name__=="__main__":
    intro_game()
    os.system("pause")
