# Question 1:
name = input("Enter your name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# Question 2:
with open("name.txt", "r") as input_file:
    print(f"Your name is {input_file.readline().strip()}")

# Question 3:
with open("numbers.txt", "r") as input_file:
    first_number = int(input_file.readline())
    second_number = int(input_file.readline())
    print(first_number + second_number)  # move outside the loop

# Question 4:
with open("numbers.txt", "r") as input_file:
    # should be named lines, numbers implies its numbers when they're actually lines/strings
    numbers = input_file.readlines()  # should be for line in file, did'nt need, shouldve done in lower loop
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += float(number)  # assumes future numbers could be non-int
    print(f"Total sum of list is {sum_of_numbers}")
