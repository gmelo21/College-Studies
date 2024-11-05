# Aug 21, 2024.

# Working with functions and function-related information, like docstrings, type hints, parameters, and so on.
# Let's calculate your K/D/A score.


# Function to run the calculations.
def calculate_battle_score(kills: int = 0, deaths: int = 0, assists: int = 0) -> float:
    """
    Args:
        kills (int): Enemies downed in battle.
        deaths (int): Deaths suffered in battle.
        assists (int): Assists on other players' kills.

    Returns:
        (float): Average battle score.
    """

    battle_score = kills + (assists / 2)

    if deaths > 0:
        battle_score = battle_score / deaths

    return battle_score


username: str = input("Your username: ").strip()

while True:
    results = input("Please type your K/D/A for the match, separating the numbers with a slash (/): ")
    results = results.replace(" ", "").split("/")

    if all(x.isdigit() for x in results):    # Verifies if all values inputted are positive numbers.
        results = [int(x) for x in results]    # Appends the numbers separately to the list.

        if len(results) == 3:    # Checks if there are only 3 values in the list.
            print(f"Player {username} has finished a match with a battle score of {calculate_battle_score(results[0], results[1], results[2]):.2f}.")
            break

        else:
            print("Invalid values.\n")

    else:
        print("Values are not numbers.\n")
