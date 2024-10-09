import requests

# way to scroll X amount of pages, way to go to specific pokemon page. make script repeatable.

# 1 - next
# 2 - previous
# find pokemon page
# find pokemon info
#


def fetch_data(url):
    if url is None:
        return None

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            print("Requisition error.")
            return None

    except:
        return None


def list_pokemon(pokemon_list, currentPage, totalPages):
    print(f"Page {currentPage} / {totalPages}")
    print()

    for pokemon in pokemon_list:
        print(pokemon["name"].capitalize())


def get_user_choice():
    return input("\nType the name of a Pokémon to see their abilities, \"next\" for the next page or \"previous\" for the previous page: ").lower().strip()


def show_abilities(pokemon_url):
    dictResponse = fetch_data(pokemon_url)
    if dictResponse:
        print("Abilities:")
        for ability in dictResponse["abilities"]:
            print(ability["ability"]["name"].capitalize())
        print("\nMoves:")
        for move in dictResponse["moves"]:
            print(move["move"]["name"].capitalize())


def find_pokemon_across_pages(name):
    mainUrl = "https://pokeapi.co/api/v2/pokemon/"

    while mainUrl:
        dictResponse = fetch_data(mainUrl)

        if dictResponse:
            for pokemon in dictResponse["results"]:
                if pokemon["name"].lower() == name:
                    print()
                    show_abilities(pokemon["url"])
                    return

            mainUrl = dictResponse["next"]

        else:
            break

    print("Pokémon not found.")
    print()
    return None


offset = 0
limit = 15

mainUrl = f"https://pokeapi.co/api/v2/pokemon/?limit=15"
currentPage = 1
totalPages = 0

while True:
    dictResponse = fetch_data(mainUrl)

    if dictResponse:
        total_count = dictResponse["count"]
        totalPages = (total_count // limit) + (1 if total_count % limit > 0 else 0)
            
        list_pokemon(dictResponse["results"], currentPage, totalPages)
        
        choice = get_user_choice()
        print()

        if choice == "next":
            mainUrl = dictResponse["next"]
            currentPage += 1

        elif choice == "previous":
            mainUrl = dictResponse["previous"]
            currentPage -= 1

        else:
            for pokemon in dictResponse["results"]:
                if pokemon["name"].lower() == choice:
                    show_abilities(pokemon["url"])
                    exit()

            else:
                searchAll = input(
                    "Pokémon not found. Search in whole database? It may take a while. ( Y/N ) ").lower().strip()

                if searchAll == "y":
                    find_pokemon_across_pages(choice)
                    exit()

                else:
                    exit()
    else:
        print("Failed to fetch data from the Pokémon API.")
        break
