import random


# Throw two 6-sided dice and add together the result
def dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    sum_of_dice = die1 + die2

    return sum_of_dice


# Central function, contains all game logic
def main():
    _ = input("Press enter to throw the dice")
    sum_of_dice = dice()

    # Check dice results and change game state accordingly
    if sum_of_dice in (7, 11):
        game_state = "W"
        print("Result: " + str(sum_of_dice) + "\n You Won!")

    elif sum_of_dice in (2, 3, 12):
        game_state = "L"
        print("Result: " + str(sum_of_dice) + "\n You Lose :(")

    else:
        game_state = "R"
        point = sum_of_dice
        print("Result: " + str(sum_of_dice) + "\nGame continues...\nThe point is" + str(sum_of_dice))

        # If a win or loss was not immediately determined, continue to have the user throwing dice until one of the
        # following 2 conditions are met.
        while game_state == "R":
            _ = input("Press enter to roll the dice")
            sum_of_dice = dice()
            print("Result: " + str(sum_of_dice))

            if sum_of_dice == point:
                game_state = "W"
                print("\n You Won!")

            elif sum_of_dice == 7:
                game_state = "L"
                print("\n You Lose :(")


main()
