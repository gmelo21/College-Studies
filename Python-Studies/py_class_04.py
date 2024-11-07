# Sep 1, 2024.

# Messing around with dictionaries. This code is a complete joke I had with a friend of mine, but it's still well made.
# Hopefully.


thingamajigs = {}
thingamajangs = {}
thingamabonks = {"Thong": "A bajillion thongies.", "Thung": "A zillion thungies."}

# Adding two keys to the first dictionary:
for n in range(2):
    thing = input("Choose a thing: ").capitalize().strip()   # Key for the first dictionary.
    thingies = input("How many thingies? ").capitalize().strip()   # Item for the key in the first dictionary.
    thingamajigs[thing] = thingies    # Adds it to the dictionary.

print()

# Adding two keys to the second dictionary:
for n in range(2):
    thang = input("Choose a thang: ").capitalize().strip()   # Key for the second dictionary.
    thangies = input("How many thangies? ").capitalize().strip()   # Item for the key in the second dictionary.
    thingamajangs[thang] = thangies    # Adds it to the dictionary.

thingaminator = {1: thingamajigs, 2: thingamajangs, 3: thingamabonks}   # Dictionary which stores the two dictionaries we created, plus one more that was already here.

print("\nThese are your dictionaries: ")

print(f"1 - {thingaminator[1]}")
print(f"2 - {thingaminator[2]}")
print(f"3 - {thingaminator[3]}")

print("\nWhy don't you try to print one of the things/thangs, in one of the dictionaries? ")

selectionDictionary = input("Type in the number of one of the dictionaries: ").strip()    # Select one of the dictionary numbers.
selectionItem = input("Type in the name of one of the items: ").capitalize().strip()   # Select one of the items by their name.

print(f"The thing \"{selectionItem}\" has \"{thingaminator[int(selectionDictionary)][selectionItem]}\" itemies!")
