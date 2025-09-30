win = 0
import random
random_int = random.randint(1, 10)
print(f"Random integer: {random_int}")

while win == 0:
    guess=(int(input("Guess a number 1-10: ")))
    if guess == random_int:
        print("You gamble succefuly")
        win=1

    elif guess > random_int:
        print("Lower")

    elif guess < random_int:
        print("Higher")