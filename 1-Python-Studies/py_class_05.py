# Sep 14, 2024.

# Little "sets" study for good measure. Nothing special, just so I can say I did something today.
# Sorry for disappearing my GitHub fans, exams and some other stuff got in the way. For the record, I was still studying!


# First, let's create two sets so I can show you a little something.
myFavoriteNumberAndWord = {1, True}
mySecondFavoriteNumberAndWord = {False, 0}

print(f"Here is a set informing you of my favorite number and word: {myFavoriteNumberAndWord}\nWait - where is the word?")
# "1" and "True" count as the same element, and sets do not accept repeated elements. Therefore, the first declared stays.
# Same is true for "0" and "False", look:
print(f"\nAnyway, here's my second favorite ones: {mySecondFavoriteNumberAndWord}\nIs this some kind of twisted joke?!")

# Now let's get to the real stuff. Let's create two sets in two different ways, one of them empty.
myFavoriteColors = set()
myFavoriteFoods = {"orange", "apple", "broccoli", "other healthy food", "pizza"}

# Here are some ways to add elements to sets:
myFavoriteColors.add("orange")
myFavoriteColors.update(["blue", "red", "green", "pink"])
# When adding multiple elements, they need to be a list, or else it would iterate through each character of the string.

# Here are how we could display each element in a set:
print("\nMy favorite colors:")
for x in myFavoriteColors:
    print(x)

# Or the easier way:
print("\nMy favorite foods:")
print(myFavoriteFoods)

# Now let's manipulate those sets a bit.
# The union of two sets:
myFavoriteStuff = myFavoriteFoods.union(myFavoriteColors)
myFavoriteStuff = myFavoriteFoods | myFavoriteColors
# Both examples return the same thing.
print(f"\nSum of my favorite stuff: {myFavoriteStuff}")
# Notice how orange was in both sets, but since we can't have repeated elements, it appears only once.

# The intersection of two sets:
commonWords = myFavoriteFoods.intersection(myFavoriteColors)
commonWords = myFavoriteFoods & myFavoriteColors
# Both examples return the same thing.
print(f"\nCommon words between food set and colors set: {commonWords} Orange is in both!")

# The difference between two sets:
notCommonWords = myFavoriteFoods.difference(myFavoriteColors)
notCommonWords = myFavoriteFoods - myFavoriteColors
# Both examples return the same thing.
print(f"\nWords in food set that are not in the colors set: {notCommonWords} Orange is not here!")

# How to erase a single element from a set:
myFavoriteFoods.discard("other healthy food")

# Or the cooler way to do it with multiple elements:
foodsToRemove = ["orange", "apple", "broccoli"]
myFavoriteFoods = set(filter(lambda x: x not in foodsToRemove, myFavoriteFoods))
# Returns True for elements not in foodsToRemove but in myFavoriteFoods, therefore adding them to a 
# new set to be attributed to myFavoriteFoods.

# There's another way to erase an element from a set, but it's riskier.
# If you try to use .remove on an element that doesn't exist, you get an error.
try:
    myFavoriteFoods.remove("beans")
except Exception as e:
    print("\nAn exception occurred:", type(e).__name__)
    # Using .discard does not give you an exception, but also does not tell you if the element
    # already existed or not. Both could be important.
    myFavoriteFoods.discard("beans")
    # No error, see?

# Here's the update food set, with my actual favorite food.
print(f"\nMy favorite food is: {str(myFavoriteFoods)[1:-1:]}")
