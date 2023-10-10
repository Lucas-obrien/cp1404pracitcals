"""
Wimbledon prac 5
estimate: 30 mins
actual:

"""
import csv

champion_to_wins = {}
wimbledon_finals = []
with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    rows = csv.reader(in_file, delimiter=",")
    for row in rows:
        wimbledon_finals.append(row)

for match in wimbledon_finals:
    try:
        champion_to_wins[match[2]] += 1
    except KeyError:
        champion_to_wins[match[2]] = 1
print(wimbledon_finals)
print(champion_to_wins)
