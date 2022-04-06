# Imports go here
import random


def dice():
    # Write some code that will generate two random numbers up to 6 and add them together
    rel1 = random.randint(0, 6)
    rel2 = random.randint(0, 6)
    ans = str(rel1) + str(rel2)
    print(ans)
    return()


def main():
    #= input("Press enter to throw the dice")
    points = 0
    rel1 = random.randint(0, 6)
    rel2 = random.randint(0, 6)
    ans = rel1 + rel2
    if ans == (7, 11):
        print("You rolled " + str(ans) + "You Win!")
        points + 1
        print(points)
    elif ans == (2, 3, 12):
        print("You rolled " + str(ans) + "You Lose!")
    else:
        print(str(ans)


#main()