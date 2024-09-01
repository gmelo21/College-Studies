# Messing around with dictionaries. This code is a complete joke I had with a friend of mine, but it's still well made.
# Hopefully.

thingamajigs = {}
thingamajangs = {}
thingamabonks = {"Thong": "A bajillion thongies.", "Thung": "A zillion thungies."}

for n in range(2):
    thing = input("Choose a thing: ").capitalize().strip()
    thingies = input("How many thingies? ").capitalize().strip()
    thingamajigs[thing] = thingies

print()

for n in range(2):
    thang = input("Choose a thang: ").capitalize().strip()
    thangies = input("How many thangies? ").capitalize().strip()
    thingamajangs[thang] = thangies

thingaminator = {1: thingamajigs,
                 2: thingamajangs,
                 3: thingamabonks
                 }

print("\nThese are your dictionaries: ")

print(f"1 - {thingaminator[1]}")
print(f"2 - {thingaminator[2]}")
print(f"3 - {thingaminator[3]}")

print("\nWhy don't you try to print one of the things/thangs, in one of the dictionaries? ")

selectionDictionary = input("Type in the number of one of the dictionaries: ").capitalize().strip()
selectionItem = input("Type in the name of one of the items: ").capitalize().strip()

print(f"The thing \"{selectionItem}\" has \"{thingaminator[int(selectionDictionary)][selectionItem]}\" itemies!")
