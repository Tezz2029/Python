"""
Find out how many months, weeks and days left if we live for 90 years and print the result using fString
"""

print("Enter your current age -")
age = int(input())

yearsLeft = 90 - age
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"Years Left - {yearsLeft} \n Months Left - {monthsLeft} \n Weeks Left {weeksLeft} \n Days Left {daysLeft}")