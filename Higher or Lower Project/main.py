import random
from game_data import data
from art import logo

print(logo)
score = 0
game = True
def higher_lower_game ():

    global score

    while game:


        a = random.choice(data)

        remaining_choices = [item for item in data if item != a]

        b = random.choice(remaining_choices)

        print(f"Compare A: {a['name']}")
        print(f"Against B: {b['name']}")

        a_or_b = input("Who has more follower? Type 'A' or 'B': ").lower()



        if a_or_b == "a" and a ['follower_count'] > b ['follower_count']:
            score += 1
            print(f"You're right! Current score : {score}")
        elif a_or_b == "b" and b ['follower_count'] > a ['follower_count']:
            score += 1
            print(f"You're right! Current score : {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break

higher_lower_game()