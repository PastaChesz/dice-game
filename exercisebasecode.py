# Imports go here
import random


def dice():
    # Write some code that will generate two random numbers up to 6 and add them together
    rel1 = random.randint(1, 6)
    rel2 = random.randint(1, 6)
    ans = rel1 + rel2
    return (ans)


def main():
    _ = input('Press enter to throw the dice')

    score = 0

    ans = dice()
    if ans in (7, 11):
        print("You rolled " + str(ans) + " You Win!")
    elif ans in (2, 3, 12):
        print("You rolled " + str(ans) + " You Lose!")
    else:
        repeat = True
        jeff = ans
        print(str(ans))
        while repeat:
            score = score + 1
            print("Your score is - ", score)
            _ = input("Press enter to roll")
            ans = dice()
            print(ans)
            if ans == (7):
                print("You rolled " + str(ans) + " You Lose!")
                print("You scored ", score, "points!")
                repeat = False
            elif ans == jeff:
                print("You win!")
                print("You scored ", score, "points!")
                repeat = False


main()