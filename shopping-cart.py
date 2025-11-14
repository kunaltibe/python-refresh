# Shopping Cart Program
# Author: Kunal Tibe
# Description: A simple interactive shopping cart program with add, view, and total features.

items = []
prices = []
total = 0
is_shopping = True

print("--------------------Shopping Cart--------------------")

while is_shopping:
    item = input("Enter the item/s to buy (press 'q' to quit): ").capitalize()
    if item.lower() == 'q':
        is_shopping = False
    else:
        price = float(input(f"Enter the price of the {item}: $"))
        if price < 0:
            print("Price cannot be less than zero")
        else:
            items.append(item)
            prices.append(price)

print("----------------------Your Cart----------------------")
if len(items) == 0:
    print("Your cart is empty!")
else:
    print("Item/s: ", end="")
    for item in items:
        print(item, end=" ")

for price in prices:
    total += price

print(f"\nTotal: ${total:.2f}")
print("---------------Thank you for shopping----------------")
