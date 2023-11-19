"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items,
each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is
displayed on the screen.


get number of items
repeat for each item
    get item price
    total price = total price + item price

if total price > 100
    total price = total price - (total price * discount rate)

display total price

"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Item price: "))
    total_price += item_price

if total_price > 100:
    total_price = total_price - (total_price * .10)

print(f"Total price is : ${total_price:.2f}")
