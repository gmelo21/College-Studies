def bubble_sort(list):
    """
    Bubble Sort algorithm.
    Returns the number of comparisons and swaps performed.
    """
    n = len(list)
    comparisons = 0
    swaps = 0
    # Traverse the list multiple times
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            comparisons += 1
            if list[j] > list[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                list[j], list[j + 1] = list[j + 1], list[j]
                swaps += 1
    return comparisons, swaps

def selection_sort(list):
    """
    Selection Sort algorithm.
    Returns the number of comparisons and swaps performed.
    """
    n = len(list)
    comparisons = 0
    swaps = 0
    for i in range(0, n - 1):
        # Assume the current index is the smallest
        min_index = i
        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            comparisons += 1
            if list[j] < list[min_index]:
                min_index = j
        # Swap the found minimum element with the element at the current index
        list[i], list[min_index] = list[min_index], list[i]
        swaps += 1
    return comparisons, swaps

def insertion_sort(list):
    """
    Insertion Sort algorithm.
    Returns the number of comparisons and swaps performed.
    """
    n = len(list)
    comparisons = 0
    swaps = 0
    # Start with the second element as the first is considered sorted
    for i in range(1, n):
        j = i
        comparisons += 1  # Count the first comparison for this element
        # Shift elements until the correct position is found
        while j > 0:
            comparisons += 1
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                swaps += 1
                j -= 1
            else:
                break

    return comparisons, swaps

def display_sort_results(sort_function, list):
    """
    Utility function to run a sort and display the sorted list and operation counts.
    """
    # Copy the list so that the original remains unchanged for further tests
    list_copy = list.copy()
    comparisons, swaps = sort_function(list_copy)
    print(f"Sorted list: {list_copy}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Total operations: {comparisons + swaps}")

def small_list_test():
    """
    Test all sorting algorithms on a small unsorted list.
    """
    test_list = [6, 7, 4, 1, 3, 2, 5]
    print("\nBubble Sort on a small list:")
    display_sort_results(bubble_sort, test_list)
    
    print("\nSelection Sort on a small list:")
    display_sort_results(selection_sort, test_list)
    
    print("\nInsertion Sort on a small list:")
    display_sort_results(insertion_sort, test_list)

def best_case_test():
    """
    Test all sorting algorithms on a best-case scenario (list in ascending order).
    """
    ascending_list = list(range(1000))
    print("\nBubble Sort (Best Case):")
    display_sort_results(bubble_sort, ascending_list)
    
    print("\nSelection Sort (Best Case):")
    display_sort_results(selection_sort, ascending_list)
    
    print("\nInsertion Sort (Best Case):")
    display_sort_results(insertion_sort, ascending_list)

def worst_case_test():
    """
    Test all sorting algorithms on a worst-case scenario (list in descending order).
    """
    descending_list = list(range(1000, 0, -1))
    print("\nBubble Sort (Worst Case):")
    display_sort_results(bubble_sort, descending_list)
    
    print("\nSelection Sort (Worst Case):")
    display_sort_results(selection_sort, descending_list)
    
    print("\nInsertion Sort (Worst Case):")
    display_sort_results(insertion_sort, descending_list)

def menu():
    """
    Menu to select which sorting test to run.
    """
    while True:
        print("\nMenu:")
        print("1. Test sorting on a small unsorted list")
        print("2. Best-case scenario (ascending order, 1000 elements)")
        print("3. Worst-case scenario (descending order, 1000 elements)")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        match choice:
            case "1":
                small_list_test()
            case "2":
                best_case_test()
            case "3":
                worst_case_test()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")

# Start the menu system
menu()
