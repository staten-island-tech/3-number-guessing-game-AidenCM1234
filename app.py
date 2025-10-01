win = 0
import random
random_int = random.randint(1, 10)
print(f"Random integer: {random_int}")

guess_history=[]
while win == 0:
    guess=(int(input("Guess a number 1-10: ")))
    if guess == random_int:
        print("You gamble succefuly")
        win=1
        print(f"You guessed{guess_history}")

    elif guess > random_int:
        print(f"Lower then {guess}")
        guess_history.append(guess)
 
    elif guess < random_int:
        print(f"Higher then {guess}")
        guess_history.append(guess)