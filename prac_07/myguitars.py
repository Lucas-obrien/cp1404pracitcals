"""

estimation - 30 mins
actual -

"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], row[1], float(row[2])))

        for guitar in guitars:
            print(guitar)


main()
