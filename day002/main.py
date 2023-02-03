#Prince Radebe
#02 February 2023
# 100 Days of Python
#If the bill was R150, split between 5 people, with 12% tip
#Each person should pay (150 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welocme to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percentage = tip /100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")