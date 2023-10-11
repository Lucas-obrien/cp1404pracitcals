"""
Wimbledon prac 5
estimate: 30 mins
actual: 60 mins

"""
import csv


def main():
    champion_to_wins = {}
    winning_countries = []
    wimbledon_finals = []
    get_winners(wimbledon_finals)

    winning_countries = compile_winners(champion_to_wins, wimbledon_finals, winning_countries)

    display_winners(champion_to_wins, winning_countries)


def display_winners(champion_to_wins, winning_countries):
    print("Wimbledon Champions:")
    for champion, win in champion_to_wins.items():
        print(f"{champion} : {win}")
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(winning_countries)))


def compile_winners(champion_to_wins, wimbledon_finals, winning_countries):
    for match in wimbledon_finals:
        print(match)
        try:
            winning_countries.append(match[1])
            champion_to_wins[match[2]] += 1
        except KeyError:
            champion_to_wins[match[2]] = 1
    winning_countries = set(winning_countries)
    return winning_countries


def get_winners(wimbledon_finals):
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        rows = csv.reader(in_file, delimiter=",")
        for row in rows:
            wimbledon_finals.append(row)


main()
