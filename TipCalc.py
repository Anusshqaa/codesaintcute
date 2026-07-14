#Tip Calculator generator Project DAY 2

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to pay? 10, 12 or 15?"))
people = int(input("How many to split the bill?"))
Total_bill = tip / 100 * bill + bill
bill_per_person = Total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}!")





