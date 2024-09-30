print("Welcome to hte rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    if age <12:
        bill=5
        print("Child tickets are $5.")
    elif age <=18:
        bill=7
        print("Youth tickets are $7.")
    elif age >=45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill=12
        print("Adult tickets are $12.")
    photo_ticket = input("Do you want a photo ticket? Y or N. ")
    if photo_ticket == "Y":
        bill = bill + 3
        print(f"Your ticket costs +3$ more. So toal is: {bill}")

else:
    print("You are not allowed to ride the rollercoaster!")