'''
Compound Interest Calculator
Author: Kunal Tibe
Description: A simple program to calculate compound interest based on principal, rate, time, and compounding frequency.

Formula:
        A = P * (1 + r/n)^(n*t)
    where:
        A = final amount
        P = principal
        r = annual interest rate (in decimal)
        n = compounding frequency per year
        t = time in years
'''

principal = 0
rate = 0
time = 0
compounding_frequency = 0

print("-----Compound Interest Calculator-----")

while True:
    principal = float(input(f"Enter principal amount: "))
    if principal <0:
        print("Principal amount cannot be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate < 0:
        print("Interest rate cannot be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time (in years): "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

while True:
    compounding_frequency = float(input("Enter number of times interest is compounded per year: "))
    if compounding_frequency < 0:
        print("Compounding frequency cannot be less than zero")
    else:
        break

amount = principal * pow((1 + rate / (100 * compounding_frequency)), (compounding_frequency * time))
interest = amount - principal

print("--------------------------------------")
print(f"Principal: ${principal:.2f}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Compounding Frequency: {compounding_frequency} times/year")
print(f"Compound Interest: ${interest:.2f}")
print(f"Total Amount: ${amount:.2f}")