"""

estimate - 90 mins
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

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project)\n- (Q)uit\n>>> ")


def main():
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            print(choice)
        elif choice == "S":
            print(choice)
        elif choice == "D":
            print(choice)
        elif choice == "F":
            print(choice)
        elif choice == "A":
            print(choice)
        elif choice == "U":
            print(choice)
        else:
            print("Invalid choice")
        choice = input(MENU).upper()


if __name__ == '__main__':
    main()
