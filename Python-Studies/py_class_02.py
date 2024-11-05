# Aug 21, 2024.

# Working with f-strings and slicing. Super simple code after I realized 75% of it was unnecessary.
# But I want you to know it was there, so I don't look lazy for the small code.


# Function to repeat the desired text for desired length.
def repeat_for_length(text, wanted_length):
    return (text * (wanted_length//len(text) + 1))[:wanted_length:]
    # The "+1" is here so the expression always results in the exact number or above (which would be cut by slicing).
    # Easier than using math.ceil, or a condition to see if the "+1" would be necessary or not.


repeatText = input("Type the text you want to be repeated: ")  # Text to be repeated.
repeatedTextSize = int(input("Desired length for the whole text: "))    # Character size for the repeated text.

print(f"\"{repeat_for_length(repeatText, repeatedTextSize)}\"")
