"""
Program to calculate the BMI by taking input from the user
"""

print("Enter your Height in meters - ")
height = float(input())
print("Enter your Weight in kg - ")
weight = float(input())

bmi = weight / height ** 2

print("Your BMI is - ", round(bmi, 2))