# Hey all. Just as a heads-up, this program is going to create two text files in your desktop.
# Nothing big, easy to delete, and most importantly, only contains a bit of malware (joke).
# As you probably guessed, we're just studying text files manipulation.

import os

# Getting the path to your precious little desktop, and then creating our file there.
desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
filePath = os.path.join(desktopPath, "dummyFile.txt")
file = open(filePath, 'w+', encoding="utf-8")

print(f"File successfully created at \"{filePath}\"\n")

# Let's add some text to our file.
file.write("Hey there! This is a normal file.")
file.write("\nYup, absolutely normal. Nothing to see here!")
file.write("\nNow, go. On your way! Skedaddle away!")

# Let's see what we wrote in the file. Since we opened it with "w+", we can read it and write in it. The main modes are:
#   - Open existing files:
#        "r"   Open text file for reading.
#        "r+"  Open for reading and writing.
#   - Create new files, or truncates it to zero length if it already exists:
#        "w"  Open for writing.
#        "w+" Open for reading and writing.
#   - The file is created only if it does not exist. The cursor at the file is positioned at the end of it.
#        "a"  Open for writing.
#        "a+"  Open for reading and writing.

# We need to make sure the file's cursor is at the first line though, since it moves as we write in the file.
# We do this with file.seek(0).
file.seek(0)

print(file.read())
print("{End of the file.}\n")

# Why don't you try adding something to our file? C'mon, your turn!
userText = "\n" + input("Type some text to be added to our file: ")
file.write(userText)

# Since we used encoding UTF-8 when we opened the file, you could write pretty much any character without a problem.
# If that was not present, characters like "ã" might look "corrupted". Look at what you wrote:
file.seek(119)

print("\n" + file.read())
print("{End of the file.}\n")

# Wow. Truly insightful stuff. You didn't tell me you were a poet!

# We're done with that file. Let's create another one, a bit different this time.
# Always make sure to close the file after you're done with it!
file.close()

# Let's create a new file.
filePath = os.path.join(desktopPath, "dummierFile.txt")

# With this following line, we can open the file while the code is indented inside the "with" statement.
# And once we leave it, it immediately closes, by itself.
with open(filePath, 'a+', encoding="utf-8") as file:
    # Let's add the counter if this is the first time you have run this code.
    if os.path.getsize(filePath) == 0:
        file.write("Counter: 0")

    # Now, let's read the number of repetitions. Which starts at the 9th character of the file.
    file.seek(9)
    currentCount = int(file.read())
    currentCount += 1
    os.truncate(filePath, 9)
    file.write(str(currentCount))
    print("Success! Open the file to see the counter, and run this code again to increase it!")

# That's all for today folks! It's 4pm, and I've yet to eat lunch. Hope you all have wonderful days!
