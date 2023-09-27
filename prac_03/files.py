# Question 1:
name = input("Enter your name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# Question 2:
with open("name.txt", "r") as input_file:
    print(input_file.readline())

# Question 3:
with open("numbers.txt", "r") as input_file:
    numbers = input_file.readlines()
    sum_of_numbers = 0
    for number in numbers[:2]:
        sum_of_numbers += int(number)
    print(f"Total sum of list is {sum_of_numbers}")

# Question 4:
with open("numbers.txt", "r") as input_file:
    numbers = input_file.readlines()
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += float(number)
    print(f"Total sum of list is {sum_of_numbers}")
