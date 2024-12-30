import tkinter 

import random

number = random.randint(1, 10)
attempts = 0
found = False

def guess_the_number():
    global found
    global attempts
    print("Welcome to Guess the number!")
    print("I'm thinking of a number between 1 and 10.")

    while found == False:
        guess=int(input("Take a guess: "))

        if guess > number :
            print("Try again, too high.")
            attempts = attempts + 1
        
        elif guess < number :
            print("Try again, too low.")
            attempts = attempts + 1

        else:
            attempts = attempts + 1
            print(f"Well Done! It took you {attempts} tries.")
            found = True


guess_the_number()