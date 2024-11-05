# Oct 10, 2024.

# Hello GitHubbers! This code is a bit more extensive than normal, and it isn't made to study anything specific besides requests.
# As it took a bit longer to made and is a bit more complicated, I made the difficult choice to not allow my amazing sense of
# character write the comments, and instead let ChatGPT do it. This way, if you're actually confused about something, you can actually
# understand what's going on instead of reading some weird comment about how I love clouds. I won't be gone for long though.

# Enjoy!


import requests  # Import the requests library to handle HTTP requests


def fetch_data(url):
    if url is None:
        return None  # Return None if the provided URL is None

    try:
        response = requests.get(url)  # Make a GET request to the specified URL

        if response.status_code == 200:
            return response.json()  # Return the JSON response if the request was successful

        else:
            # Print an error message for unsuccessful requests
            print("Requisition error.")
            return None

    except:
        return None  # Return None if an exception occurs during the request


def list_pokemon(pokemonList, currentPage, totalPages):
    # Display the current page and total pages
    print(f"Page {currentPage} / {totalPages}")
    print()

    for pokemon in pokemonList:
        # Print the name of each Pokémon in the list
        print(pokemon["name"].capitalize())


def get_user_choice():
    # Prompt the user to select an action from the menu and return the input
    return input("\n1 - Next page. \n2 - Previous page. \n3 - Scroll multiple pages. \n4 - Go back multiple pages. \n5 - Specific Pokémon information. \n6 - Specific Pokémon page. \n\nSelect function: ").lower().strip()


def show_info(pokemonUrl):
    # Fetch data for a specific Pokémon using its URL
    dictResponse = fetch_data(pokemonUrl)
    if dictResponse:
        print("Abilities:")  # Print header for abilities
        for ability in dictResponse["abilities"]:
            # Print each ability name
            print(ability["ability"]["name"].capitalize())

        print("\nMoves:")  # Print header for moves
        # Create a list of move names
        moveList = [move["move"]["name"].capitalize()
                    for move in dictResponse["moves"]]

        # Print moves in a formatted manner (5 moves per line)
        for i in range(0, len(moveList), 5):
            print(f"{moveList[i]:<15}" +
                  (f"{moveList[i + 1]:<15}" if i + 1 < len(moveList) else "") +
                  (f"{moveList[i + 2]:<15}" if i + 2 < len(moveList) else "") +
                  (f"{moveList[i + 3]:<15}" if i + 3 < len(moveList) else "") +
                  (f"{moveList[i + 4]:<15}" if i + 4 < len(moveList) else ""))


def find_pokemon(name, totalCount):
    # URL to fetch all Pokémon
    allPokemonUrl = f"https://pokeapi.co/api/v2/pokemon/?limit={totalCount}"

    while allPokemonUrl:
        dictResponse = fetch_data(allPokemonUrl)  # Fetch data for all Pokémon

        if dictResponse:
            for pokemon in dictResponse["results"]:
                # Check if the Pokémon matches the user's input
                if pokemon["name"].lower() == name:
                    print()
                    # Show information for the found Pokémon
                    show_info(pokemon["url"])
                    input()  # Wait for user input
                    return

            else:
                break  # Exit the loop if Pokémon not found

    print("Pokémon not found.")  # Print error message if Pokémon is not found
    input()
    return None


def next_page(nextOffset, nextCurrentPage, totalCount, limit, totalPages):
    # Calculate the next page offset and current page number
    if nextOffset + limit <= totalCount:
        nextOffset += limit  # Increment offset for next page
        nextCurrentPage += 1  # Increment current page number

    else:
        # Set offset to the last page
        nextOffset = totalCount - (totalCount % limit)
        nextCurrentPage = totalPages  # Update current page to the last page

        print("Currently on last page.")  # Inform the user
        input()

    return nextOffset, nextCurrentPage  # Return updated offset and current page


def previous_page(previousOffset, previousCurrentPage, limit):
    # Calculate the previous page offset and current page number
    if previousOffset - limit >= 0:
        previousOffset -= limit  # Decrement offset for previous page
        previousCurrentPage -= 1  # Decrement current page number

    else:
        previousOffset = 0  # Set offset to the first page
        previousCurrentPage = 1  # Update current page to the first page

        print("Currently on first page.")  # Inform the user
        input()

    # Return updated offset and current page
    return previousOffset, previousCurrentPage


def next_multiple_pages(nextOffset, nextCurrentPage, nextTimes, totalCount, limit, totalPages):
    # Navigate forward by multiple pages
    for i in range(nextTimes):
        if nextOffset + limit <= totalCount:
            nextOffset += limit  # Increment offset for next page
            nextCurrentPage += 1  # Increment current page number

        else:
            nextOffset = totalCount - (totalCount % limit)  # Set to last page
            nextCurrentPage = totalPages  # Update current page to the last page

            print("Currently on last page.")  # Inform the user
            input()

            return nextOffset, nextCurrentPage  # Return updated offset and current page

    return nextOffset, nextCurrentPage  # Return updated offset and current page


def previous_multiple_pages(previousOffset, previousCurrentPage, previousTimes, limit):
    # Navigate back by multiple pages
    for i in range(previousTimes):
        if previousOffset - limit >= 0:
            previousOffset -= limit  # Decrement offset for previous page
            previousCurrentPage -= 1  # Decrement current page number

        else:
            previousOffset = 0  # Set offset to the first page
            previousCurrentPage = 1  # Update current page to the first page

            print("Currently on first page.")  # Inform the user
            input()

            # Return updated offset and current page
            return previousOffset, previousCurrentPage

    # Return updated offset and current page
    return previousOffset, previousCurrentPage


def find_pokemon_page(newOffset, name, newCurrentPage, totalCount, limit):
    # URL to fetch all Pokémon
    allPokemonUrl = f"https://pokeapi.co/api/v2/pokemon/?limit={totalCount}"

    dictResponse = fetch_data(allPokemonUrl)  # Fetch data for all Pokémon

    if dictResponse:
        for index, pokemon in enumerate(dictResponse["results"]):
            if pokemon["name"].lower() == name:  # Check if Pokémon matches the user's input
                # Calculate new offset based on the Pokémon's index
                newOffset = (index // limit) * limit
                # Calculate new current page number
                newCurrentPage = (index // limit) + 1
                return newOffset, newCurrentPage  # Return updated offset and current page

    print("Pokémon not found.")  # Print error message if Pokémon is not found
    input()
    return newOffset, newCurrentPage  # Return original offset and current page


def main():
    offset = 0  # Initialize offset for pagination
    limit = 10  # Set limit for number of Pokémon per page

    rootUrl = "https://pokeapi.co/api/v2/pokemon/"  # Base URL for Pokémon API

    currentPage = 1  # Initialize current page number
    totalPages = 0  # Initialize total pages

    while True:
        # Construct the main API URL
        mainUrl = rootUrl + f"?offset={offset}" + f"&limit={limit}"
        # Fetch data for the current page of Pokémon
        dictResponse = fetch_data(mainUrl)

        if dictResponse:
            totalCount = dictResponse["count"]  # Get total number of Pokémon
            totalPages = (totalCount // limit) + \
                (1 if totalCount % limit > 0 else 0)  # Calculate total pages

            # List Pokémon for the current page
            list_pokemon(dictResponse["results"], currentPage, totalPages)

            choice = get_user_choice()  # Get user choice for action
            print()

            match choice:  # Handle user's choice using pattern matching
                case "1":
                    offset, currentPage = next_page(
                        offset, currentPage, totalCount, limit, totalPages)  # Go to the next page

                case "2":
                    offset, currentPage = previous_page(
                        offset, currentPage, limit)  # Go to the previous page

                case "3":
                    try:
                        # Get number of pages to scroll forward
                        times = int(input("How many pages forward? ").strip())
                        offset, currentPage = next_multiple_pages(
                            offset, currentPage, times, totalCount, limit, totalPages)  # Scroll forward
                    except:
                        # Handle invalid input
                        print("Please type a valid number.")
                        input()

                case "4":
                    try:
                        # Get number of pages to go back
                        times = int(input("How many pages back? ").strip())
                        offset, currentPage = previous_multiple_pages(
                            offset, currentPage, times, limit)  # Go back multiple pages
                    except:
                        # Handle invalid input
                        print("Please type a valid number.")
                        input()

                case "5":
                    pokemonChoice = input(
                        # Get specific Pokémon name
                        "Type the name of the desired Pokémon: ").lower().strip()
                    # Search for the Pokémon
                    find_pokemon(pokemonChoice, totalCount)

                case "6":
                    pokemonChoice = input(
                        # Get specific Pokémon name
                        "Type the name of the desired Pokémon: ").lower().strip()
                    offset, currentPage = find_pokemon_page(
                        offset, pokemonChoice, currentPage, totalCount, limit)  # Find Pokémon page

                case _:
                    print("Invalid choice.")  # Handle invalid choice
                    input()

        else:
            # Inform user of failure
            print("Failed to fetch data from the Pokémon API.")
            break  # Exit the loop if data fetch fails


if __name__ == "__main__":
    main()  # Run the main function if this script is executed
