# Number Guessing Game
import random
number=random.randint(1,10)
guess= 0
attempt= 0
print("Guess the no. between 1 to 10")
while guess!= number:
    guess=int(input("Enter the guess:"))
    attempt +=1
    if guess < number:
     print("Too low")
    elif guess > number:
       print("Too high")
    else:
       print(f'Correct! The number was {number}.Attempt: {attempt}')