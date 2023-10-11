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


for match in wimbledon_finals:
    try:
        countries.append(match[1])
        champion_to_wins[match[2]] += 1
    except KeyError:
        champion_to_wins[match[2]] = 1

print("Wimbledon Champions:")
for champion, win in champion_to_wins.items():
    print(f"{champion} : {win}")

print(f"These {len(set(countries))} countries have won Wimbledon:")
print(", ".join(country for country in sorted(set(countries))))

