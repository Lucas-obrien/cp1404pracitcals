import wikipedia

choice = input("Enter a search term: ")
while choice != "":
    try:
        choice_page = wikipedia.page(choice)
        print(choice_page.title)
        print(choice_page.summary)
        print(choice_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print(f"{choice} not found")
    choice = input("Enter a search term: ")
