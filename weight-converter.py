# Weight Converter
# Author: Kunal Tibe
# Description: A simple program to convert weight between kilograms and pounds.

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or k or L or l): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {weight:.2f} {unit}")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {weight:.2f} {unit}")
else:
    print(f"Sorry, '{unit}' is an invalid unit")
