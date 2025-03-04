# Function to perform linear search
def linear_search(list, target):
    """
    Searches for the target value in the list using linear search.
    Returns the index of the target if found, otherwise returns -1.
    """
    for i in range(len(list)):
        if list[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if not found

# Function to perform binary search
def binary_search(list, target):
    """
    Searches for the target value in a sorted list using binary search.
    Returns the index of the target if found, otherwise returns -1.
    """
    start, end = 0, len(list) - 1
    while start <= end:
        mid = (start + end) // 2  # Find the middle index
        if list[mid] == target:
            return mid  # Target found
        elif target > list[mid]:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half
    return -1  # Return -1 if not found

# Function to update a value in the sorted list using binary search
def binary_search_update(list, target, new_value):
    """
    Searches for the target value in a sorted list using binary search.
    If found, replaces it with new_value and prints 5 elements before and after (including the new value).
    """
    start, end = 0, len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            list[mid] = new_value  # Update the value
            # Define the range to display (5 elements before and after)
            start_index = max(0, mid - 5)
            end_index = min(len(list) - 1, mid + 5)
            print(f"Updated portion of the list: {list[start_index:end_index + 1]}")
            return
        elif target > list[mid]:
            start = mid + 1  # Continue search in the right half
        else:
            end = mid - 1  # Continue search in the left half
    return -1  # Return -1 if not found

# Function to count comparisons in linear search
def linear_search_comparisons(list, target):
    """
    Counts the number of comparisons made in a linear search.
    Returns the number of comparisons made until the target is found.
    """
    comparisons = 0
    for i in range(len(list)):
        comparisons += 1
        if list[i] == target:
            return comparisons  # Return the number of comparisons
    return comparisons  # If not found, return the total comparisons made

# Function to count comparisons in binary search
def binary_search_comparisons(list, target):
    """
    Counts the number of comparisons made in a binary search.
    Returns the number of comparisons made until the target is found.
    """
    start, end = 0, len(list) - 1
    comparisons = 0
    while start <= end:
        mid = (start + end) // 2
        comparisons += 1  # Increment comparison count
        if list[mid] == target:
            return comparisons  # Return the number of comparisons
        elif target > list[mid]:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half
    return comparisons  # If not found, return the total comparisons made

# Recursive implementation of binary search
def binary_search_recursive(list, target, start, end):
    """
    Searches for the target value in a sorted list using recursive binary search.
    Returns the index of the target if found, otherwise returns -1.
    """
    if start > end:
        return -1  # Base case: if search space is empty, return -1
    mid = (start + end) // 2
    if list[mid] == target:
        return mid  # Target found
    elif target > list[mid]:
        return binary_search_recursive(list, target, mid + 1, end)  # Search in right half
    else:
        return binary_search_recursive(list, target, start, mid - 1)  # Search in left half

# Menu-driven function to interact with the user
def menu():
    """
    Displays a menu that allows the user to choose between different search operations.
    Handles input and performs the selected operation.
    """
    original_numbers = list(range(10000))  # Create a sorted list of numbers from 0 to 9999
    numbers = original_numbers.copy()  # Create a copy to modify

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Binary Search Update")
        print("4. Linear Search Comparisons")
        print("5. Binary Search Comparisons")
        print("6. Binary Search Recursive")
        print("7. Reset List")
        print("8. Exit")
        choice = input("Choose an option: ")

        # Process user choice using match-case
        match choice:
            case "1":
                target = int(input("Enter the number to search: "))
                result = linear_search(numbers, target)
                print(f"Result: {result}")
            case "2":
                target = int(input("Enter the number to search: "))
                result = binary_search(numbers, target)
                print(f"Result: {result}")
            case "3":
                target = int(input("Enter the number to update: "))
                new_value = int(input("Enter the new value: "))
                binary_search_update(numbers, target, new_value)
            case "4":
                target = int(input("Enter the number to search: "))
                result = linear_search_comparisons(numbers, target)
                print(f"Comparisons: {result}")
            case "5":
                target = int(input("Enter the number to search: "))
                result = binary_search_comparisons(numbers, target)
                print(f"Comparisons: {result}")
            case "6":
                target = int(input("Enter the number to search: "))
                result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
                print(f"Result: {result}")
            case "7":
                numbers = original_numbers.copy()  # Reset list to original
                print("List has been reset.")
            case "8":
                print("Exiting...")
                break  # Exit the loop
            case _:
                print("Invalid option. Please try again.")  # Handle invalid input

# Run the menu function to start the program
menu()
