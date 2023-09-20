"""
MENU = menu options
import password stars
import broken score

function main
    display MENU
    get menu choice
    while menu choice != Q
        if menu choice = G
            get valid score
        else if menu choice = P
            display the result
        else if menu choice = S
            display stars
        else
            display invalid choice
        display MENU
        get menu choice

function get valid score
    get score
    while score > 100 or < 0
        invalid score
        get score
    return score
"""

from score import display_score

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Program that displays a menu with options, then validates a score, prints * equal to the score or displays a
        rating of a score."""
    print(MENU)
    menu_choice = input("choose: ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            user_score = get_valid_score()
        elif menu_choice == "P":
            print(display_score(user_score))
        elif menu_choice == "S":
            print(show_total_stars(user_score))
        else:
            print("invalid choice")
        print()
        print(MENU)
        menu_choice = input("choose: ").upper()

    print("Farewell")


def show_total_stars(user_score):
    """Returns * equal to the input amount."""
    return "*" * user_score


def get_valid_score():
    """Gets a user's score from input, then validates based on boundary conditions, then returns score."""
    user_score = int(input("Enter score: "))
    while user_score > 100 or user_score < 0:
        print("Invalid score")
        user_score = int(input("Enter score: "))

    return user_score


main()
