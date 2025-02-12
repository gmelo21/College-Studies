# Function to calculate the player's battle score based on K/D/A (Kills/Deaths/Assists)
def calculate_battle_score(kills: int = 0, deaths: int = 0, assists: int = 0) -> float:
    """
    Args:
        kills (int): Enemies downed in battle.
        deaths (int): Deaths suffered in battle.
        assists (int): Assists on other players' kills.

    Returns:
        float: The player's average battle score.
    """
    # Calculate battle score: kills + half of assists
    battle_score = kills + (assists / 2)

    # If deaths occurred, adjust the battle score based on the number of deaths
    if deaths > 0:
        battle_score = battle_score / deaths

    return battle_score


# Get the player's username
username: str = input("Your username: ").strip()

# Continuously ask for the player's K/D/A until valid input is provided
while True:
    # Prompt for K/D/A and split the input by slash (e.g., 10/3/5)
    results = input(
        "Please type your K/D/A for the match, separating the numbers with a slash (/): ")
    results = results.replace(" ", "").split("/")

    # Check if all values are digits (positive numbers)
    if all(x.isdigit() for x in results):
        # Convert the results to integers
        results = [int(x) for x in results]

        # Ensure there are exactly 3 values (K, D, A)
        if len(results) == 3:
            # Print the player's battle score formatted to 2 decimal places
            print(
                f"Player {username} has finished a match with a battle score of {calculate_battle_score(results[0], results[1], results[2]):.2f}.")
            break
        else:
            print("Invalid values. Please enter 3 numbers.\n")
    else:
        print("Values are not numbers. Please enter valid numbers.\n")
