import os

# Get the path to the desktop and create a file on it
desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
filePath = os.path.join(desktopPath, "dummyFile.txt")
file = open(filePath, 'w+', encoding="utf-8")

print(f"File successfully created at \"{filePath}\"\n")

# Write some text into the file
file.write("Hey there! This is a normal file.")
file.write("\nYup, absolutely normal. Nothing to see here!")
file.write("\nNow, go. On your way! Skedaddle away!")

# Reposition the file cursor to the beginning to read the contents
file.seek(0)

# Read and print the contents of the file
print(file.read())
print("{End of the file}\n")

# Allow the user to add their own text to the file
userText = "\n" + input("Type some text to be added to our file: ")
file.write(userText)

# Since we used UTF-8 encoding, special characters can be written without issue
# If UTF-8 was not specified, characters like "ã" might be corrupted
file.seek(119)

# Display the updated contents of the file
print("\n" + file.read())
print("{End of the file}\n")

# Close the first file to avoid leaving it open
file.close()

# Now, create another file with a different behavior
filePath = os.path.join(desktopPath, "dummierFile.txt")

# Use the 'with' statement to automatically handle opening and closing the file
with open(filePath, 'a+', encoding="utf-8") as file:
    # If the file is empty (first run), initialize a counter
    if os.path.getsize(filePath) == 0:
        file.write("Counter: 0")

    # Read the current counter value from the file
    file.seek(9)
    currentCount = int(file.read())
    currentCount += 1

    # Truncate the file to remove the old counter value, then write the updated count
    os.truncate(filePath, 9)
    file.write(str(currentCount))

    print("Success! Open the file to see the counter, and run this code again to increase it!")
