# Little "sets" study for good measure. Nothing special, just so I can say I did something today.
# Sorry for disappearing my GitHub fans, exams and some other stuff got in the way. For the record, I was still studying!

myFavoriteColors = set()
myFavoriteFoods = {"orange", "apple", "broccoli", "other healthy food", "pizza"}
myFavoriteNumberAndWord = {1, True}
mySecondFavoriteNumberAndWord = {False, 0}

print(f"Here is a set informing you of my favorite number and word: {myFavoriteNumberAndWord}\nWait - where is the word?")
# 1 and True count as the same element, and sets do not accept repeated elements. Therefore, the first declared stays.
# Same is true for 0 and False, look:
print(f"\nAnyway, here's my second favorite ones: {mySecondFavoriteNumberAndWord}\nIs this some kind of twisted joke?!")

# Here are some ways to add elements to sets:
myFavoriteColors.add("orange")
myFavoriteColors.update(["blue", "red", "green", "pink"])
# Needs to be a list, or else it would iterate through each character of the string.

# Here are how we could display each element in a set:
print("\nMy favorite colors:")
for x in myFavoriteColors:
    print(x)

# Or the easier way:
print("\nMy favorite foods:")
print(myFavoriteFoods)

# The union of two sets, both returning the same thing:
myFavoriteStuff = myFavoriteFoods.union(myFavoriteColors)
myFavoriteStuff = myFavoriteFoods | myFavoriteColors
print(f"\nSum of my favorite stuff: {myFavoriteStuff}")

# The intersection of two sets, both returning the same thing:
commonWords = myFavoriteFoods.intersection(myFavoriteColors)
commonWords = myFavoriteFoods & myFavoriteColors
print(f"\nCommon words between food set and colors set: {commonWords} Orange is in both!")

# The difference between two sets, both returning the same thing:
notCommonWords = myFavoriteFoods.difference(myFavoriteColors)
notCommonWords = myFavoriteColors - myFavoriteFoods
print(f"\nWords in food set that are not in the colors set: {notCommonWords} Orange is not here!")

# How to erase a single element from a set:
myFavoriteFoods.discard("other healthy food")

# Or the cooler way to do it with multiple elements:
foodsToRemove = ["orange", "apple", "broccoli"]
myFavoriteFoods = set(filter(lambda x: x not in foodsToRemove, myFavoriteFoods))
# Returns True for elements not in foodsToRemove, therefore adding them to the new set attributed to myFavoriteFoods.

# If you try to use .remove on an element that doesn't exist, you get an error.
try:
    myFavoriteFoods.remove("beans")
except Exception as e:
    print("\nAn exception occurred:", type(e).__name__)
    # However, using .discard does not give you an error,
    myFavoriteFoods.discard("beans")

# Here's the update food set, with only my actual favorite food.
print(f"\nMy favorite food is: {str(myFavoriteFoods)[1:-1:]}")

