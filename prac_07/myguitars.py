"""

estimation - 30 mins
actual -

"""

import csv
from collections import namedtuple
from guitar import Guitar
from operator import itemgetter

FILENAME = "guitars.csv"
INDEX_YEAR = 1


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        NewGuitar = namedtuple('Guitar', 'name, year, cost')
        for row in reader:
            guitars.append(NewGuitar._make(row))
        guitars.sort(key=itemgetter(INDEX_YEAR))
        for guitar in guitars:
            print(guitar)


main()
