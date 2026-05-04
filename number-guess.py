import random

number = random.randint(1, 100)

attempts = 0

while True:
    attempts += 1
    input_number = int(input("Guess the number: "))
    if input_number == number:
        print("Congratulations! You guessed the number.")
        break
    elif input_number < number:
        print("Too low! Try again.")
    elif input_number > number:
        print("Too high! Try again.")
    else:
        print("Sorry, that's not the correct number. Try again!")
    
    if attempts >= 5:
        print(f"Sorry, you've used all {attempts} attempts. The number was {number}.")
        break

if attempts < 5:
    print(f"You guessed the number in {attempts} attempts.")