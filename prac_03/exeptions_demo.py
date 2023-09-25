"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? line 10, 11, where the input is specified as int
2. When will a ZeroDivisionError occur? line 12, where the calculation is performed
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Error check the denominator so it != 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
