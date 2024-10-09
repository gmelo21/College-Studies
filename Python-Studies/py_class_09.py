import requests


def fetch_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            print("Requisition error.")
            return None

    except Exception as error:
        print(f"Error: {error}")
        return None


def list_pokemon(pokemon_list):
    for pokemon in pokemon_list:
        print(pokemon["name"].capitalize())


def get_user_choice():
    return input("\nType the name of a Pokémon to see their abilities, \"next\" for the next page or \"previous\" for the previous page: ").lower().strip()


def show_abilities(pokemon_url):
    dictResponse = fetch_data(pokemon_url)
    if dictResponse:
        for ability in dictResponse["abilities"]:
            print(ability["ability"]["name"].capitalize())


mainUrl = "https://pokeapi.co/api/v2/pokemon/"

while True:
    dictResponse = fetch_data(mainUrl)

    if dictResponse:
        list_pokemon(dictResponse["results"])
        choice = get_user_choice()
        print()

        if choice == "next":
            mainUrl = dictResponse["next"]
            
        elif choice == "previous":
            mainUrl = dictResponse["previous"]

        else:
            for pokemon in dictResponse["results"]:
                if pokemon["name"] == choice:
                    show_abilities(pokemon["url"])
                    exit()

            else:
                print("Name not found.")
                exit()
