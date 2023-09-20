"""
Get user score and print a rating
"""
# score.py
import random


def main():
    score = float(input("Enter score: "))
    print(display_score(score))
    print(display_score(random.randint(0, 100)))


def display_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


# main()
