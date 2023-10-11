"""
Wimbledon prac 5
estimate: 30 mins
actual:

"""
import csv

champion_to_wins = {}
wimbledon_finals = []
countries = []


with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    rows = csv.reader(in_file, delimiter=",")
    for row in rows:
        wimbledon_finals.append(row)
