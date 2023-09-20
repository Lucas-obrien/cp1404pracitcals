"""
Get user score and print a rating
"""
# score.py
import random


def main():
    """Program that gets a user's score, then displays a rating of the score."""
    score = float(input("Enter score: "))
    print(display_score(score))
    print(display_score(random.randint(0, 100)))


def display_score(score):
    """Takes a score and returns a rating based on boundary conditions."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

# commented out so importing this file wouldn't cause issues
# main()
