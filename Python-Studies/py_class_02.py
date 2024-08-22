# Working with f-strings, slicing, and other random challenges.

def repeat_for_length(text, wanted) -> str:
    """
    Args:
        text (str): The text supposed to be repeated.
        wanted (int): Desired length of the repeated text.

    Returns:
        (str): Repeated text in the wanted length.
    """

    return (text * (wanted//len(text) + 1))[:wanted:]
    # The "+1" is here so the expression always results in an exact number or above, which would be cut by slicing.
    # Easier than using math.ceil, or a condition to see if the "+1" would be necessary or not.


def repeat_for_length_with_spaces(text, wanted) -> str:
    """
    Args:
        text (str): The text supposed to be repeated.
        wanted (int): Desired length of the repeated text.

    Returns:
        (str): Repeated text in the wanted length.
    """

    return ((text + " ") * (wanted//len(text) + 1))[:wanted:].strip()


repeatedText = "Nnngh... "
endingText = "Forefathers one and all, bear witness!"
fullTextSize = 50
repeatedTextSize = fullTextSize - len(repeatedText)

print(f"{repeat_for_length(repeatedText, repeatedTextSize)}! {endingText}", end = " (Dragon noises)")
print()

# If you wanted the repeated words to be separated, but not want the risk of the repeated sentence to end
# with a whitespace, you could run the other function.

print(f"{repeat_for_length_with_spaces("Hello!", 38)} ... why are you even reading this?")
print()

# In this case, the whitespaces do NOT count as a character for the total length. If you wanted them to count, the
# sentence would either need to be able to end with a whitespace for cases where its length is a divisor of the "wanted"
# variable, or run the risk of the sentence being a character short if you use .strip(), removing that whitespace.

# The following examples all count whitespace as characters for the full sentence:

print(("Example similar to the first function. " * (78//len("Exemplo na primeira função. ") + 1))[:78:])
# Has whitespaces counting for the total characters and no .strip(), meaning the print will have 78 characters.

print(("Example similar to the first function, with .strip(). " * (108//len("Exemplo na primeira função com .strip(). ") + 1))[:108:].strip())
# Has whitespaces counting for the total characters and .strip(), meaning the print will have 107 characters in case
# the 108th character was a whitespace (like in this case).

print((("Example similar to the second function." + " ") * (80//(len("Exemplo na segunda função.") + 1) + 1))[:80:])
# Has whitespaces (added separately) counting for the total characters and no .strip(), meaning the print will have
# 80 characters.

print((("Example similar to the second function, with .strip()." + " ") * (110//(len("Exemplo na segunda função com .strip().") + 1) + 1))[:110:].strip())
# Has whitespaces (added separately) counting for the total characters and .strip(), meaning the print will have 109
# characters in case the 110th character was a whitespace (like in this case).

# Those were a LOT of comments in one single Python file. But who cares? I learned, and you maybe did, too.