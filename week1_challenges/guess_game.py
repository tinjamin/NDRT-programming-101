import random 
import math

answer = random.randint(0,101) 

a = int(input("1 for computer vs computer or 2 for computer vs human: "))
if a == 2:
    while True: 
        guess = int(input("Please guess a number from 1-100: "))
        if guess == answer: 
            print("Congratualations. That's the right number!") 
            break 
        elif guess > answer:
            print("Your guess was too high.")
        else: 
            print("Your guess was too low.")
else:
    print(f"This is the number that the computer is trying to guess: {answer}")
    for tries in range(0, 999):
        if tries == 0:
            comp_guess = random.randint(0,101)
        elif comp_guess == answer:
            print(f"number was {comp_guess}")
            print(f"it took the computer {tries} tries")
            break
        else: 
            if comp_guess < answer: 
                print(f"{comp_guess}")
                comp_guess = random.randint(comp_guess, 101)
                
            else:
                print(f"{comp_guess}")
                comp_guess = random.randint(0, comp_guess)

