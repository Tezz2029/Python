"""
Check whether the user can ride the roller coaster or not.
And then count the final ticket price
"""

bill = 150
photo = 50
totalBill = 0
photoBill = 0

age = int(input("Enter Your Age - "))

if age >= 14 and age < 80:
    height = float(input("Enter Your Height in 'feet' - "))

    if height >= 5.625 and height < 8:
        weight = float(input("Enter Your Weight in 'kg' - "))

        if weight >= 47.63 and weight < 200:
            print("You can ride the Roller Coaster")
            wantPhoto = input("Do you want to click a photo - ")
            if wantPhoto == 'y' or wantPhoto == 'Y':
                photoBill = bill + photo

            else:
                photoBill = bill

            if age < 18:
                totalBill = photoBill
                print(f"Your Bill is {totalBill}")

            if age >= 18:
                totalBill = photoBill + bill
                print(f"Your Bill is {totalBill}")

        else:
            print("Sorry You cant ride the Roller Coaster")

    else:
        print("Sorry You cant ride the Roller Coaster")

else:
    print("Sorry You cant ride the Roller Coaster")




