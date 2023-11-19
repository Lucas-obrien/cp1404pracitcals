"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program that gets student data and displays in a specified format"""
    data = get_data()
    print_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_information = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_information.append(parts)

    input_file.close()
    return subject_information


def print_subject(subjects):
    """Take in data from a nested list, then print each individual part from each index"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:3} students")


main()
