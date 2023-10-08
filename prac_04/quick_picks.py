import random

MAXIMUM_GENERATED_NUMBERS = 6
MAXIMUM_RANDOM_NUMBERS = 45

number_of_quickpicks = int(input("How many quick picks? "))

for i in range(number_of_quickpicks):
    quickpick_numbers = []
    random_number = 0
    for j in range(MAXIMUM_GENERATED_NUMBERS):
        while random_number in quickpick_numbers or random_number == 0:
            random_number = random.randint(1, MAXIMUM_RANDOM_NUMBERS)
        quickpick_numbers.append(random_number)
    print(" ".join(f"{number:2}" for number in sorted(quickpick_numbers)))

