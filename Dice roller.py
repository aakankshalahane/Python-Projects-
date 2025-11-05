import random

while True:
    roll = input("Roll dice? (x/y): ").lower()
    if roll == 'x':
        print("You rolled:", random.randint(1, 6))
    else:
        print("Goodbye!")
        break
