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
                save_projects(file_header_names,
                              projects)  # ignore error; won't reach here without a project being loaded
            else:
                print("Nothing to save")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            print(f"That day is/was {date.strftime('%A')}")
            print(date.strftime("%d/%m/%Y"))
            print(choice)
        elif choice == "U":
            print(choice)
        else:
            print("Invalid choice")
        choice = input(MENU).upper()


def filter_projects(projects):
    date_string = input("Show projects that start after date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()  # e.g., "30/9/2022"
    filtered_projects = [project for project in projects
                         if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
    for project in filtered_projects:
        print(project)


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
    incomplete_projects = [project for project in projects if int(project.completion_percentage) < 100]
    incomplete_projects = sorted(incomplete_projects, key=lambda project: project.priority)
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    left_over_projects = [project for project in projects if project not in incomplete_projects]
    for project in left_over_projects:
        print(project)


if __name__ == '__main__':
    main()
