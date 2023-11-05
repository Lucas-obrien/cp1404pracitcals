"""
Guitar Module for prac_07
Opens and reads a csv file and constructs guitar objects, then saves to a csv file.
estimation - 30 mins
actual - 60 mins
"""

import csv
from collections import namedtuple
from guitar import Guitar
from operator import itemgetter

FILENAME = "guitars.csv"
INDEX_NAME = 0
INDEX_YEAR = 1
INDEX_COST = 2


def main():
    """Program that reads and adds guitars to a csv file."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        NewGuitar = namedtuple('Guitar', 'name, year, cost')
        for row in reader:
            print(Guitar(row[INDEX_NAME], row[INDEX_YEAR], float(row[INDEX_COST])))
            guitars.append(NewGuitar._make(row))

    guitars.sort(key=itemgetter(INDEX_YEAR))
    for guitar in guitars:
        print(guitar)

    name = input("Enter guitar name: ")
    while name != "":
        year = input("Enter year: ")
        cost = input("Enter cost: $")
        guitars.append(NewGuitar._make([name, year, cost]))
        name = input("Enter guitar name: ")

    guitars.sort(key=itemgetter(INDEX_YEAR))

    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(",".join(guitar), file=out_file)


main()
