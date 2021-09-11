# importing the random and math module
import random
import math

# taking inputs
lower = int(input("Enter lower range number: "))
upper = int(input("Enter upper range number: "))

# generating random number between upper and lower
x = random.randint(lower, upper)
print("you have only", round(math.log(upper- lower+1,2)), "chances to guess !")
print("")

# initialising the number of guesses
count = 0

# for calculation of min number of guesses depends upon range
while count < math.log(upper- lower+1,2):
    count += 1

    # taking guessing number as input
    guess = int(input("guess a number: "))

    # condition testing
    if x == guess:
        print("CONGRATULATIONS! you did it in", count, "try")
        # once guessed correct loop will break
        break

    elif x>guess:
        print("you guessed too small.. Try Again!")

    elif x < guess:
        print("you guessed too high.. Try Again!")

# if guessing is more than required guesses
if count > math.log(upper-lower+1, 2):
    print("the number is %d " % x)
    print('\tBetter Luck Next Time!')






