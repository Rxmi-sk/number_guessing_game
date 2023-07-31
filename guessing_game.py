import random
import os
import json


def get_random_val(min,max):
    val=random.randint(min,max)
    print("The random number is:",val)
    return val

def get_score(guess_val, rand_val):
    score_val = 0
    if guess_val == rand_val:
        score_val=score_val+rand_val
        
    else:
        score_val=-1
    
    return score_val

def game():
    guessesTaken=0
    scorecard={}
    name=str(input("Hello, what is your name?\n"))
    if name!="":
        print("Hello ", name, ",", "Pick a number from 0 to 10 (including 0 & 10)\n\n=================")
    else:
        print("Hello Player,", "Pick a number from 0 to 10 (including 0 & 10)\n\n=================")
        name="Player"


    scorecard[name]=0


    while guessesTaken < 10:
        while True:
            try:
                guessesTaken= guessesTaken+1
                print("Remaining spins: ", 11-guessesTaken)
                guess_val=int(input("\nYour number: "))
                assert guess_val > -1 and guess_val < 11
                rnd_val=get_random_val(0,10)
                scorecard[name] = scorecard[name] + get_score(guess_val,rnd_val)
                print("Your score is:", scorecard[name])
                print("\n=================")
                break
            except ValueError:
                print("Value must be a whole number")
                guessesTaken= guessesTaken-1
            except AssertionError:
                print("Value must be between 0 and 10 (including 0 & 10)")
                guessesTaken= guessesTaken-1

                
        
       

    if scorecard[name]>0:
        print("\nCongratulations, your score is", scorecard[name], ", You've won!!!")

    else:
        print("\nYour score is", scorecard[name],", You have lost :(")

    
    sc = open("scoreboard_file","a")
    json.dump(scorecard,sc)
    sc.close()


    print("\nCurrent scoreboard:")
    sc1 = open("scoreboard_file","r")
    print(sc1.readlines()[0].replace('}{','}\n{'))
    
