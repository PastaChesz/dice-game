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
    _ = input("Press enter to throw the dice")
    # Write the game code here. You need to compare your dice result against the game rules to determine whether it
    # has been won, lost or is ongoing.


main()