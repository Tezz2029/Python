"""
WAP to check whether the user input year is a Leap Year or not
"""

print("Enter a Year -")
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print(f"Entered Year {year} is a Leap Year")

elif year % 100 != 0 and year % 400 == 0:
    print(f"Entered Year {year} is a Leap Year")

else:
    print(f"Entered Year {year} is not a Leap Year")