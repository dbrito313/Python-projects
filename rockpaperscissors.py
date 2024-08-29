import random

playerdecision = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

computerdecision = random.randint(0,2)

print(f"Computer chose {computerdecision}.")

if playerdecision >= 3 or playerdecision < 0:
  print("You typed an invalid number. RIP")
elif playerdecision == 0 and computerdecision == 2:
  print("You won.")
elif computerdecision == 0 and playerdecision == 2:
  print("You lose.")
elif playerdecision == computerdecision:
  print("It's a draw.")
elif playerdecision > computerdecision:
  print("You won.")
elif playerdecision < computerdecision:
  print("You lose.")