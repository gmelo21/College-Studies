import json

# Create the Python script (py_class_08_part2.py) that will interact with the JSON file
with open("py_class_08_part2.py", "w+") as file:
    file.write("""
import json

# Open the previously saved JSON file and load its content into a Python dictionary
# JSON is useful for storing data that can be easily converted into Python objects
with open("file.json", "r") as file:
    cloudsDict = json.load(file)

    # The data from the file is now stored in a Python dictionary
    print(f"\"cloudsDict\" is back to a \"{type(cloudsDict).__name__}\"!\n")

    # Print each cloud category (key) and its corresponding types (values)
    for key in cloudsDict.keys():
        print(key)
        # Display the types of clouds, converting the list to a string for better readability
        print(str(cloudsDict[key])[1:-1:])
        print()

# Demonstrating how to store data in JSON format within the script itself
# json.dumps converts Python objects into JSON strings
cloudText = "I wish I was a cloud sometimes. Letting the wind take me wherever it wants. Above all."
jsonCloudText = json.dumps(cloudText)
print(jsonCloudText)

# Overwriting the previous cloud text with a new string and printing the result as a JSON string
cloudText = "Nature would cheer when I rained. But when all cleared up, nature would cheer again."
jsonCloudText = json.dumps(cloudText)
print(jsonCloudText)

# Showing how string concatenation works with JSON data, though this is not a recommended practice for valid JSON
cloudText = "Shikamaru was right when he said he wished to be a cloud."
jsonCloudText += json.dumps(cloudText)
print(jsonCloudText)

# Demonstrating concatenation of numbers in JSON, where numbers do not require quotation marks
number = 1
jsonNumber = json.dumps(number)
print(jsonNumber)

# Adding another number to the existing JSON data and printing the result
number = 2
jsonNumber += json.dumps(number)
print(jsonNumber)

# A more appropriate method for adding numbers while maintaining valid JSON format
number = 1
jsonNumber = json.dumps(number)
print(jsonNumber)

# Adding a second number while ensuring the result is valid JSON by first converting it back to an integer
number = 2
jsonNumber = json.dumps(json.loads(jsonNumber) + number)
print(jsonNumber)
""")

# Now, create a JSON file with cloud information
with open("file.json", "w+") as file:
    lowClouds = ["Stratus", "Stratocumulus",
                 "Cumulus", "Nimbostratus", "Cumulonimbus"]
    mediumClouds = ["Altostratus", "Altocumulus",
                    "Nimbostratus", "Cumulonimbus"]
    highClouds = ["Cirrostratus", "Cirrus", "Cirrocumulus", "Cumulonimbus"]

    # Create a dictionary to store different types of clouds
    cloudsDict = {"1 - Low clouds": lowClouds,
                  "2 - Medium clouds": mediumClouds,
                  "3 - High clouds": highClouds}

    # Dump the dictionary into the JSON file with proper formatting (indentation and ensuring non-ASCII characters are preserved)
    json.dump(cloudsDict, file, indent=2, ensure_ascii=False)

    # Print the cloud categories for the user to select
    for key, value in cloudsDict.items():
        print(f"{key}")

    # User input to select the type of clouds to learn about
    answer = input(
        "\nInput the number related to the height of the clouds you want to learn about: ")

    match answer:
        case "1":
            print("\nLow clouds")
            print(
                f"{str(cloudsDict['1 - Low clouds']).replace("'", '')[1:-1:]}")
        case "2":
            print("\nMedium clouds")
            print(
                f"{str(cloudsDict['2 - Medium clouds']).replace("'", '')[1:-1:]}")
        case "3":
            print("\nHigh clouds")
            print(
                f"{str(cloudsDict['3 - High clouds']).replace("'", '')[1:-1:]}")

    # Simple interaction to demonstrate how cloud data can be accessed and displayed
    print("Cloud types are pretty cool! Let's move on to the next example.")
