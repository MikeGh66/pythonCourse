print("Welcome to the tip calculator.")
total = float(input("What is the total bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

pay = float(tip/100 *total+total)/people

final_amount = round(pay, 2)

print(f"Each person soulg pay: ${final_amount}")