def repeat_for_length(text, wanted_length):
    """
    Repeats the given text to fit the specified length

    Args:
        text (str): The text to be repeated
        wanted_length (int): The total length of the output string

    Returns:
        str: A string of the desired length containing repeated text
    """
    # Repeat the text enough times to exceed the desired length, then truncate to the exact length
    return (text * (wanted_length // len(text) + 1))[:wanted_length]


# Get user input for the text to repeat and the desired total length
repeat_text = input("Type the text you want to be repeated: ")
repeated_text_size = int(input("Desired length for the whole text: "))

# Print the formatted repeated text enclosed in quotes
print(f'"{repeat_for_length(repeat_text, repeated_text_size)}"')
