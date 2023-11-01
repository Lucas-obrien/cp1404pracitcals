"""

estimate - 90 minutes
actual -


    Load projects
    (Prompt the user for a filename to load projects from and load them)
    Save projects
    (Prompt the user for a filename to save projects to and save them)
    Display projects
    (Display two groups: incomplete projects; completed projects, both sorted by priority)
    Filter projects by date
    (Ask the user for a date and display only projects that start after that date, sorted by date)
    Add new project
    (Ask the user for the inputs and add a new project to memory)
    Update project
    (Choose a project, then modify the completion % and/or priority - leave blank to retain existing values)

"""
import datetime
import csv
# from collections import namedtuple
# from operator import itemgetter
from project_management import ProjectManagement

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit\n>>> ")
FILENAME = 'projects.txt'


def main():
    projects = []
    choice = input(MENU).upper()

    while choice != "Q":
        if choice == "L":
            projects, file_header_names = load_projects()
        elif choice == "S":
            if projects:
                # ignore error; won't reach here without a project being loaded
                save_projects(file_header_names, projects)
            else:
                print("Nothing to save")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(MENU).upper()


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    choice = is_valid_project("Pick a project: ", projects)
    print(projects[choice])
    new_percentage = int(input("New percentage: "))
    if not new_percentage:
        new_percentage = projects[choice].completion_percentage
    new_priority = input("New Priority: ")
    if not new_priority:
        new_priority = projects[choice].priority
    projects[choice] = ProjectManagement(projects[choice].name, projects[choice].start_date, new_priority,
                                         projects[choice].cost_estimate, new_percentage)


def is_valid_project(output_string, projects):
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input(output_string))
            if projects[choice] and choice < 0:
                print("Must be >= 0")
            else:
                valid_choice = True

        except (IndexError, ValueError):
            print("Invalid number")

    return choice


def add_project(projects):
    name = is_valid_string("name: ")
    start_date = is_valid_date("Start date (d/m/yyyy): ")  # e.g., "30/9/2022"
    priority = is_valid_number("Priority: ")
    cost_estimate = is_valid_number("Cost estimate: $")
    completion_percentage = is_valid_number("Completion percentage: ")
    projects.append(ProjectManagement(name, start_date, priority, cost_estimate, completion_percentage))


def is_valid_number(output_string):
    valid_number = False
    while not valid_number:
        try:
            number_choice = int(input(output_string))
            valid_number = True
        except ValueError:
            print("Invalid number")
    return number_choice


def is_valid_string(input_string):
    valid_string = False
    while not valid_string:
        try:
            choice = input(input_string)
            if not choice:
                print("cannot be blank")
            else:
                valid_string = True
        except ValueError:
            print(f"Invalid {input_string}")

    return choice


def is_valid_date(output_string):
    valid_date = False
    while not valid_date:
        try:
            date = input(output_string)
            datetime.datetime.strptime(date, "%d/%m/%Y")
            valid_date = True
        except ValueError:
            print("Invalid date format")
    return date


def filter_projects(projects):
    try:
        date_string = input("Show projects that start after date (d/m/yyyy): ")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()  # e.g., "30/9/2022"
        filtered_projects = [project for project in projects
                             if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Incorrect format for date")


def save_projects(file_header_names, projects):
    with open('test.txt', "w") as out_file:
        print(file_header_names.strip(), file=out_file)
        for project in projects:
            print(project, file=out_file)


def load_projects():
    with open(FILENAME, "r") as in_file:
        file_header_names = in_file.readline()
        reader = csv.reader(in_file, delimiter='\t')
        projects = []
        for row in reader:
            print(row)
            projects.append(ProjectManagement(row[0], row[1], row[2], row[3], row[4]))
    return projects, file_header_names


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.is_incomplete()]
    incomplete_projects = sorted(incomplete_projects, key=lambda project: project.priority)
    complete_projects = [project for project in projects if not project.is_incomplete()]
    complete_projects = sorted(complete_projects, key=lambda project: project.priority)
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in complete_projects:
        print(project)


if __name__ == '__main__':
    main()
