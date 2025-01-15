import random
print("Welcome to Guess the Number!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is?")

correct_answer = random.randint(1,100)

game = True
attempts = 0

while game:
    guess = int(input("Make a guess:"))
    attempts += 1

    if guess > correct_answer:
        print("Too high! Try again.")
    elif guess < correct_answer:
        print("Too low! Try again.")
    else:
        print(f"Correct! You guessed the number in {attempts} tries.")
        game = False