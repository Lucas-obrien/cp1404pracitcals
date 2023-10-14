NAME_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Bitter Lemon": "#cae00d",
    "Celadon": "#ace1af",
    "Deep Peach": "#ffcba4",
    "Eggshell": "#f0ead6",
    "Ferrari Red": "#ff2800",
    "Glaucous": "#6082b6",
    "Harlequin": "#3fff00",
    "Jungle Green": "4cbb17",
    "Iceberg": "#71a6d2"

}

print(NAME_TO_CODE)
choice = input("Enter a colour name: ").title()
while choice != "":
    try:
        print(NAME_TO_CODE[choice])
    except KeyError:
        print("Invalid Name")
    choice = input("Enter a colour name: ").title()
