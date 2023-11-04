"""

estimate - 90 minutes
actual -



"""
import datetime
import csv
# from collections import namedtuple
# from operator import itemgetter
from project_management import ProjectManagement

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date"
        "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ")
DEFAULT_LOAD_FILE = 'projects.txt'
NO_MAXIMUM = "No Max"
DEFAULT_SAVE_FILE = 'projects.txt'
MINIMUM_PRIORITY = 0
MAXIMUM_PRIORITY = 9
MINIMUM_PERCENTAGE = 0
MAXIMUM_PERCENTAGE = 100
MINIMUM_COST = 0


def main():
    """Project management tool."""
    choice = input(MENU).upper()
    projects, file_header_names = load_file(DEFAULT_LOAD_FILE)  # load file at start of program
    while choice != "Q":
        if choice == "L":
            file_header_names, projects = manual_load_file()
        elif choice == "S":
            manual_save_file(file_header_names, projects)
        elif choice == "D":
            display_all_current_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)

        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    save_file(file_header_names, projects, DEFAULT_SAVE_FILE)


def manual_save_file(file_header_names, projects):
    """Prompt user for a file name, then write list into it."""
    save_file_name = input("Input file name to save to: ")
    # ignore error; won't reach here without a project being loaded
    save_file(file_header_names, projects, save_file_name)


def manual_load_file():
    """Prompt user for a file name, then try to load, on fail set list to blank."""
    try:
        file_name = input("Enter file name to load: ")
        projects, file_header_names = load_file(file_name)
    except FileNotFoundError:
        print("File not found, loading blank list")
        projects = []
    return file_header_names, projects  # Ignore error; appears due to try/except


def update_project(projects):
    """Select and update a current project."""
    for i, project in enumerate(projects):
        print(i, project)
    choice = is_valid_project("Pick a project: ", projects)
    new_percentage = is_valid_number("New percentage: ", MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE)
    if not new_percentage:
        new_percentage = projects[choice].completion_percentage
    new_priority = int(is_valid_number("New Priority: ", MINIMUM_PRIORITY, MAXIMUM_PRIORITY))
    if not new_priority:
        new_priority = projects[choice].priority
    projects[choice] = ProjectManagement(projects[choice].name, projects[choice].start_date,
                                         new_priority, projects[choice].cost_estimate,
                                         new_percentage)


def is_valid_project(output_string, projects):
    """Determine if a project exists."""
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
    return choice  # Ignore error; appears due to try/except


def add_project(projects):
    """Add a project object to a list."""
    print("Let's add a new project")
    name = is_valid_string("name: ")
    start_date = is_valid_date("Start date (d/m/yyyy): ")  # e.g., "30/9/2022"
    priority = is_valid_number("Priority: ", MINIMUM_PRIORITY, MAXIMUM_PRIORITY)
    cost_estimate = float(is_valid_number("Cost estimate: $", MINIMUM_COST, NO_MAXIMUM))
    completion_percentage = is_valid_number("Completion percentage: ",
                                            MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE)
    projects.append(ProjectManagement(name, start_date, priority,
                                      cost_estimate, completion_percentage))


def is_valid_number(output_string, minimum_number, maximum_number):
    """Determine if a number is valid."""
    valid_number = False
    while not valid_number:
        try:
            number_choice = int(input(output_string))
            if minimum_number <= number_choice <= maximum_number:
                valid_number = True
            else:
                error_string = f"between {minimum_number} and {maximum_number} inclusive" if (
                        maximum_number != NO_MAXIMUM) else f"greater than {minimum_number}"
                print(f"Number must be {error_string}")
        except ValueError:
            print("Invalid number")
    return number_choice  # Ignore error; appears due to try/except


def is_valid_string(input_string):
    """Determine if a string is valid."""
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
    return choice  # Ignore error; appears due to try/except


def is_valid_date(output_string):
    """Determine if a date is valid."""
    valid_date = False
    while not valid_date:
        try:
            date = input(output_string)
            datetime.datetime.strptime(date, "%d/%m/%Y")
            valid_date = True
        except ValueError:
            print("Invalid date format")
    return date  # Ignore error; appears due to try/except


def filter_projects(projects):
    """Sort projects based on an entered date value"""
    try:
        date_string = input("Show projects that start after date (d/m/yyyy): ")
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()  # e.g.,"30/9/2022"
        filtered_projects = [project for project in projects
                             if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
                             > filter_date]
        filtered_projects.sort(key=lambda project: project.start_date, reverse=True)
        display_projects(filtered_projects)
    except ValueError:
        print("Incorrect format for date")


def save_file(file_header_names, projects, save_file_name):
    """Open and save to a specified file."""
    with open(save_file_name, "w", encoding="UTF-8") as out_file:
        print(file_header_names, file=out_file)
        for project in projects:
            project_details = [project.name, project.start_date, str(project.priority),
                               str(project.cost_estimate), str(project.completion_percentage)]
            print("\t".join(project_details), file=out_file)


def load_file(file_name):
    """Read in a specified file."""
    projects = []
    with open(file_name, "r", encoding="UTF-8") as in_file:
        file_header_names = in_file.readline().strip()
        reader = csv.reader(in_file, delimiter='\t')
        for row in reader:
            projects.append(ProjectManagement(row[0], row[1], int(row[2]),
                                              float(row[3]), int(row[4])))
    return projects, file_header_names


def display_all_current_projects(projects):
    """Create two lists of complete/incomplete projects and display."""
    incomplete_projects = [project for project in projects if project.is_incomplete()]
    incomplete_projects.sort(key=lambda project: project.priority)
    print("Incomplete projects: ")
    display_projects(incomplete_projects)
    complete_projects = [project for project in projects if project not in incomplete_projects]
    complete_projects.sort(key=lambda project: project.priority)
    print("Complete projects: ")
    display_projects(complete_projects)


def display_projects(projects):
    """Print passed in projects."""
    for project in projects:
        print(project)


if __name__ == '__main__':
    main()
