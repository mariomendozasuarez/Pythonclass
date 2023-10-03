#Bill calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator ")
total_bill = float(input("What was the total bill? "))
per_bill = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
per_bill /= 100 
per_bill += 1 
people = int(input("How many people to split the bill? "))
bill_splitted = (total_bill*per_bill)/people
new_bill_splitted = f"{bill_splitted:.2f}"
print(f"Each person should pay: $ {new_bill_splitted} ")

