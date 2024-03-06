"""
Write a Program to calculate the BMI by taking input from the user and also print his weight type
"""

print("Enter your Height in meters - ")
height = float(input())
print("Enter your Weight in kg - ")
weight = float(input())

bmi = weight / height ** 2
bmi = round(bmi, 2)

print("Your BMI is - ", bmi)

if bmi <= 18.4:
    print(f"Your BMI is {bmi} and you are Underweight.")
elif bmi <= 24.9:
    print(f"Your BMI is {bmi} and you have a Normal Weight.")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi} and you are Overweight.")
elif bmi <= 34.9:
    print(f"Your BMI is {bmi} and you are Obese.")
else:
    print(f"Your BMI is {bmi} and you are Clinically Obese.")

