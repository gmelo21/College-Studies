# Taking user input for text
text = input("Type in your text: ")

# Vowel checker
print("\nVowel checker")

# Define a string of vowels and initialize the vowel count
vowelList = "aeiou"
vowelCount = 0

# Loop through each character in the input text and check if it's a vowel
for i in text.lower():
    if i in vowelList:
        vowelCount += 1

# Print the number of vowels found in the input text
print("\t\"{1}\" has {0} vowels.".format(vowelCount, text))

# Word separator and counter
print("\nWord separator and counter")

# Remove any non-alphanumeric characters except spaces and apostrophes
textNotSpecial = "".join(i for i in text if (
    i.isalnum() or i == " " or i == "'"))

# Split the text into individual words
individualWords = textNotSpecial.split(" ")

# Print the list of words and the word count
if len(individualWords) == 1:
    print("\tThe word present is: {0}.".format(str(individualWords)[1:-1]))
    print("\tThere is {0} word.".format(len(individualWords)))
else:
    print("\tThe words present are: {0}.".format(str(individualWords)[1:-1]))
    print("\tThere are {0} words.".format(len(individualWords)))

# Number checker
print("\nNumber checker")

# Initialize lists and counters for even and odd numbers
numberList = []
evenCount = 0
oddSummer = 0
evenList = []
oddList = []

# Prompt the user to enter 10 numbers
for i in range(10):
    numberList.append(int(input("\t\tType in number {0}: ".format(i + 1))))

# Loop through the list of numbers to classify them as even or odd
for i in numberList:
    if i % 2 == 0:
        evenCount += 1
        evenList.append(i)
    else:
        oddSummer += i
        oddList.append(i)

# Print the highest, lowest, and average of the numbers, as well as the even and odd numbers
print("\tThe highest number is {0}, the lowest is {1}, and the average is {2}.".format(
    max(numberList), min(numberList), sum(numberList) / 10))
print("\tThere are {0} even numbers there, and the sum of all the odd numbers are {1}.".format(
    evenCount, oddSummer))
print("\tThe even numbers are: {0} and the odd numbers are: {1}.".format(
    str(evenList)[1:-1], str(oddList)[1:-1]))
