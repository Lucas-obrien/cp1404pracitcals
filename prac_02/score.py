"""
Get user score and print a rating
"""

import random


def main():
    score = float(input("Enter score: "))
    print(validate_score(score))
    print(validate_score(random.randint(0, 100)))


def validate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
