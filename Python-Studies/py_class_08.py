# Oct 10, 2024.

# Hello my GitHubbers! You know an aspect of nature I regularly think is underappreciated? Clouds.
# And JSON files, too. Which is a coincidence, because we are working with both today!

# This file will create two other files in your computer, one JSON file and another Python script, which
# you'll have to run yourself later. First, let's import JSON.


import json

# We'll write the script for the other Python file too.

with open("py_class_08_part2.py", "w+") as file:
    file.write("""
# Welcome back! Let's import JSON.

import json

# And now, let's open the JSON file we created on the last script. Similarly to normal text files, information can be stored
# there, but even easier with JSON, being able to turn back into Python code if we so please!

with open("file.json", "r") as file:
    cloudsDict = json.load(file)

    # Now, "cloudsDict" is back to being a Python dictionary, and not only a JSON file.

    print(f"\"cloudsDict\" is back to a \"{type(cloudsDict).__name__}\"!\n")

    for key in cloudsDict.keys():
        print(key)
        print(str(cloudsDict[key])[1:-1:])
        print()

        # See? We can now also access that dictionary from other files. Now, it may be a single dictionary, but you can potentially
        # store so much in it and make several files be able to access that information for a bigger, badder project.

# We're gonna see another way to use JSON in Python, which is storing it internally. The method "dumps" can convert a Python
# object into a JSON string, whereas the method "dump" (used on the first script) can be used for writing/dumping JSON to a
# file/socket, as we did to "file.json".

# Let's put some text in this JSON.

cloudText = "I wish I was a cloud sometimes. Letting the wind take me wherever it wants. Above all."
jsonCloudText = json.dumps(cloudText)
print(jsonCloudText)

# As you can see, no new files were created. As we are assigning a value to a variable, trying to dump more items
# would lead to the prior ones being overwritten, instead of concatenated, as if we were writing a file.

cloudText = "Nature would cheer when I rained. But when all cleared up, nature would cheer again."
jsonCloudText = json.dumps(cloudText)
print(jsonCloudText)

# See? The old text vanished.
# You could try to do this:

cloudText = "Shikamaru was right when he said he wished to be a cloud."
jsonCloudText += json.dumps(cloudText)
print(jsonCloudText)

# Although, in doing so, you lose the ability of loading the JSON back into Python, for it is no longer valid JSON.
# It becomes simply two strings glued together, not a list or a concatenation.

# That does happen because of the quotation marks, though. If we were to put numbers, this would happen:

number = 1
jsonNumber = json.dumps(number)
print(jsonNumber)

number = 2
jsonNumber += json.dumps(number)
print(jsonNumber)

# Because of the lack of the quotation marks, they were concatenated successfully, and became one string.
# However, even if we were to specify them being integers, they wouldn't be added together, for being
# inserted separately, not caring what was there before.

# The correct way to do it would be:

number = 1
jsonNumber = json.dumps(number)
print(jsonNumber)

number = 2
jsonNumber = json.dumps(json.loads(jsonNumber) + number)
print(jsonNumber)

# Which you don't need me to tell it's not practical here. We know which number was last inserted, and could just
# sum 2 to it and them dump the result by itself. But in case the numbers were added separately, from other devices,
# et cetera, then this would be a plausible solution.

# This is a simple demonstration, and it's up to you (us) to figure out what we could do with it. 
# Besides adding 1 and 2 together.
""")

# Now that everything is done, let's create our JSON file and study about the main types of clouds.

with open("file.json", "w+") as file:
    lowClouds = ["Stratus", "Stratocumulus",
                 "Cumulus", "Nimbostratus", "Cumulonimbus"]

    mediumClouds = ["Altostratus", "Altocumulus",
                    "Nimbostratus", "Cumulonimbus"]

    highClouds = ["Cirrostratus", "Cirrus", "Cirrocumulus", "Cumulonimbus"]

    cloudsDict = {"1 - Low clouds.": lowClouds,
                  "2 - Medium clouds.": mediumClouds, "3 - High clouds.": highClouds}
    
    # Now, we dump this dictionary into the JSON file. We set an indentation of 2 spaces, and disable
    # "ensure_ascii", so any punctuation doesn't get corrupted along the way.

    json.dump(cloudsDict, file, indent=2, ensure_ascii=False)
    
    # The JSON part is done. The rest is for flavor, and it is nothing we haven't seen before.
    # Just some user input so you can choose which clouds you want to learn the names of.

    for key, value in cloudsDict.items():
        print(f"{key}")

    answer = input(
        "\nInput the number related to the height of the clouds you want to learn about: ")

    match answer:

        case "1":

            print("\nLow clouds:")
            print(
                f"{str(cloudsDict["1 - Low clouds."]).replace("'", "")[1:-1:]}")

        case "2":

            print("\nMedium clouds:")
            print(
                f"{str(cloudsDict["2 - Medium clouds."]).replace("'", "")[1:-1:]}")

        case "3":

            print("\nHigh clouds:")
            print(
                f"{str(cloudsDict["3 - High clouds."]).replace("'", "")[1:-1:]}")

    # Simple enough right? Interesting stuff. Clouds are pretty cool! Anyway, let's go to the next file, to show the
    # extent of JSON usage.
