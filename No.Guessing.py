import random

num = random.randint(1,99)
guess = None

while guess != num:
    guess= input("Guess a number b/w 1 to 99 :")
    guess = int(guess)

    if guess == 18:
        print("Congratulation !! You Won !!🥳")
        break 
    else:
        print("You Lost Better Luck next time 🫡")