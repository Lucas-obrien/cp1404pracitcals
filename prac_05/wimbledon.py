"""
Wimbledon prac 5
estimate: 30 mins
actual:

"""

with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    for row in in_file:
        print(row)