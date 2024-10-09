import requests

import json

try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")

    if response.status_code == 200:
        dictResponse = response.json()

        for item in dictResponse["results"]:
            print(f"{item["name"].capitalize()}")

        choice = input(
            "Type the name of a Pokémon for more info or \"next\" for the next page: ").lower().strip()

        if choice == "next":
            response = requests.get(dictResponse[choice])
            print(response)

        else:
            PokeListCount = 0

            for item in dictResponse["results"]:
                if dictResponse["results"][PokeListCount]["name"] == choice:
                    response = requests.get(dictResponse["results"][PokeListCount]["url"])
                    dictResponse = response.json()
                    print(json.dumps(dictResponse["abilities"], indent=4)[1:-1:])
                    break
                    
                PokeListCount += 1

    else:
        print("Requisition error.")

except Exception as error:
    print(f"Error: {error}")
