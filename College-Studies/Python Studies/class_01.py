# Working with functions and function-related information, like docstrings, type hints, parameters, and so on.

def calculate_battle_score(kills: int = 0, deaths: int = 0, assists: int = 0) -> float:
    """
    Args:
        kills (int): Enemies downed in battle.
        deaths (str): Deaths suffered in battle.
        assists (int): Assists on other players' kills.

    Returns:
        (float): Average battle score.
    """

    if deaths == 0:
        battle_score = kills + (assists / 2)

    else:
        battle_score = (kills + (assists / 2)) / deaths

    return battle_score


username: str = input("Your username: ").strip()

while True:
    results = input("Please type your K/D/A for the match, separating the numbers with a slash (/): ")
    results = results.replace(" ", "").split("/")

    if all(x.isdigit() for x in results):
        results = [int(x) for x in results]

        if len(results) == 3:
            print(f"Player {username} has finished a match with a battle score of {calculate_battle_score(results[0], results[1], results[2]):.2f}.")
            break

        else:
            print("Invalid values.\n")

    else:
        print("Values are not numbers.\n")