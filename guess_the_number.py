import random

number = random.randint(0, 100)
attempts = 10
print(f"You have {attempts} attempts to guess the number.")

for chance in range(1, attempts+1):
    guess = int(input("\nGuess the number: "))

    if guess == number:
        print(f"\nCongratulations! You guessed it. The number is {number}!")
        break
    elif guess < number:
        print("Too low.")
        remaining_attempts = attempts - chance
        if remaining_attempts == 0:
            print(f"Out of attempts. The number was {number}.")
        else:
            print(f"You have {remaining_attempts} attempts left.")
    else:
        print("Too high.")
        remaining_attempts = attempts - chance
        if remaining_attempts == 0:
            print(f"Out of attempts. The number was {number}.")
        else:
            print(f"You have {remaining_attempts} attempts left.")
