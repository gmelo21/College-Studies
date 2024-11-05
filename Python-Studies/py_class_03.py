# Aug 23, 2024.

# Some class exercises with strings and some numbers, nothing special.


text = input("Type in your text: ")

# Vowel checker.

print("\nVowel checker:")

vowelList = "aeiou"
vowelCount = 0

for i in text.lower():
    if i in vowelList:
        vowelCount += 1

print("\t\"{1}\" has {0} vowels.".format(vowelCount, text))

# Word separator and counter.

print("\nWord separator and counter:")

textNotSpecial = "".join(i for i in text if (i.isalnum() or i == " " or i == "'"))
individualWords = textNotSpecial.split(" ")

if len(individualWords) == 1:
    print("\tThe word present is: {0}.".format(str(individualWords)[1:-1]))
    print("\tThere is {0} word.".format(len(individualWords)))
else:
    print("\tThe words present are: {0}.".format(str(individualWords)[1:-1]))
    print("\tThere are {0} words.".format(len(individualWords)))

# Number checker.

print("\nNumber checker:")

numberList = []
evenCount = 0
oddSummer =  0
evenList = []
oddList = []

for i in range(10):
    numberList.append(int(input("\t\tType in number {0}: ".format(i + 1))))

for i in numberList:
    if i % 2 == 0:
        evenCount += 1
        evenList.append(i)

    else:
        oddSummer += i
        oddList.append(i)

print("\tThe highest number is {0}, the lowest is {1}, and the average is {2}.a".format(max(numberList), min(numberList), sum(numberList) / 10))
print("\tThere are {0} even numbers there, and the sum of all the odd numbers are {1}.".format(evenCount, oddSummer))
print("\tThe even numbers are: {0} and the odd numbers are: {1}.".format(str(evenList)[1:-1], str(oddList)[1:-1]))
