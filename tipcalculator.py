#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = float(input("What was the total of the meal?\n"))
tip = int(input("How much do you want to tip?\n"))
nr_of_ppl = int(input("How many people to split the bill?\n"))

bill_with_tip = total * (1+tip / 100)
pay_per_person = bill_with_tip / nr_of_ppl
rounded_pay = round(pay_per_person, 2)
rounded_pay = "{:.2f}".format(rounded_pay)

print(f"Each one has to pay {rounded_pay}€")

