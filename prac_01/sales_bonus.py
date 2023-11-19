"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


get sales
bonus rate = 1.1
if sales >= 1000
    bonus rate = 1.15
final pay = sales * bonus rate
display final pay
"""

sales = float(input("Sale amount: $"))
while sales >= 0:
    bonus_rate = .10  # Seeing the answers shows that this is extra work for the computer
    if sales >= 1000:  # Make this if statement the "calculate the bonus" area, rather than outside
        bonus_rate = .15  # Works fine for a single run without a loop as bonus_rate will be at minimum 10%
    bonus_pay = sales * bonus_rate
    print(f"Bonus pay is ${bonus_pay}")
    sales = float(input("Total user sales: $"))
print(len("hello there"))
