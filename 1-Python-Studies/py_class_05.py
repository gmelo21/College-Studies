# Creating two sets with some values to demonstrate set behavior.
myFavoriteNumberAndWord = {1, True}
mySecondFavoriteNumberAndWord = {False, 0}

# Displaying the first set. Note that both 1 and True are considered the same in a set.
print(
    f"Here is a set informing you of my favorite number and word: {myFavoriteNumberAndWord}\nWait - where is the word?")
# The set removes duplicates, so only one element (1 and True are the same) will appear in the set.
# Similarly, 0 and False are treated as the same element.
print(
    f"\nAnyway, here's my second favorite ones: {mySecondFavoriteNumberAndWord}\nIs this some kind of twisted joke?!")

# Creating two sets, one empty and the other with some initial values.
myFavoriteColors = set()
myFavoriteFoods = {"orange", "apple",
                   "broccoli", "other healthy food", "pizza"}

# Adding elements to a set using the `add()` and `update()` methods.
myFavoriteColors.add("orange")
myFavoriteColors.update(["blue", "red", "green", "pink"])

# Displaying each element of the `myFavoriteColors` set using a loop.
print("\nMy favorite colors:")
for x in myFavoriteColors:
    print(x)

# Alternatively, print the entire `myFavoriteFoods` set directly.
print("\nMy favorite foods:")
print(myFavoriteFoods)

# Performing set operations: union of two sets.
myFavoriteStuff = myFavoriteFoods.union(myFavoriteColors)
myFavoriteStuff = myFavoriteFoods | myFavoriteColors
# Both union methods give the same result.
print(f"\nSum of my favorite stuff: {myFavoriteStuff}")
# Elements that appear in both sets will only appear once due to the nature of sets.

# Performing set operations: intersection of two sets.
commonWords = myFavoriteFoods.intersection(myFavoriteColors)
commonWords = myFavoriteFoods & myFavoriteColors
# Both intersection methods give the same result.
print(
    f"\nCommon words between food set and colors set: {commonWords} Orange is in both!")

# Performing set operations: difference between two sets.
notCommonWords = myFavoriteFoods.difference(myFavoriteColors)
notCommonWords = myFavoriteFoods - myFavoriteColors
# Both difference methods give the same result.
print(
    f"\nWords in food set that are not in the colors set: {notCommonWords} Orange is not here!")

# Removing a single element from the `myFavoriteFoods` set using `discard()`.
myFavoriteFoods.discard("other healthy food")

# Removing multiple elements from a set using `filter()` and a lambda function.
foodsToRemove = ["orange", "apple", "broccoli"]
myFavoriteFoods = set(
    filter(lambda x: x not in foodsToRemove, myFavoriteFoods))
# The lambda function filters out the elements present in `foodsToRemove` from the set.

# Attempting to remove an element from the set using `remove()`. This raises an exception if the element is not found.
try:
    myFavoriteFoods.remove("beans")
except Exception as e:
    print("\nAn exception occurred:", type(e).__name__)
    # Using `discard()` instead of `remove()` prevents an exception if the element is not found.
    myFavoriteFoods.discard("beans")
    # No exception raised.

# Displaying the updated `myFavoriteFoods` set.
print(f"\nMy favorite food is: {str(myFavoriteFoods)[1:-1:]}")
