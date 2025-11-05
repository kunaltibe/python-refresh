# Countdown Timer
# Author: Kunal Tibe
# Description: A simple countdown program using the time module.

# using for loop
import time

print("-------------COUNTDOWN TIMER---------------")
timer = int(input("Enter the time to begin: "))
print("\n--------------TIMER STARTS-----------------")
time.sleep(0.5)

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

#----------------------------------------------------

# using while loop
'''
import time

print("-------------COUNTDOWN TIMER---------------")
timer = int(input("Enter the time to begin: "))
print("\n--------------TIMER STARTS----------------")
time.sleep(0.5)

while timer:
    seconds = timer % 60
    minutes = (timer // 60) % 60
    hours = (timer // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    timer -= 1
    time.sleep(1)

print("TIME'S UP!")
'''