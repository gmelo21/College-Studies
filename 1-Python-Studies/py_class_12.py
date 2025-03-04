def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binary_search(list, target):
    start, end = 0, len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif target > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_update(list, target, new_value):
    start, end = 0, len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            list[mid] = new_value
            start_index = max(0, mid - 5)
            end_index = min(len(list) - 1, mid + 5)
            print(f"Updated portion of the list: {list[start_index:end_index + 1]}")
            return
        elif target > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def linear_search_comparisons(list, target):
    comparisons = 0
    for i in range(len(list)):
        comparisons += 1
        if list[i] == target:
            return comparisons
    return comparisons

def binary_search_comparisons(list, target):
    start, end = 0, len(list) - 1
    comparisons = 0
    while start <= end:
        mid = (start + end) // 2
        comparisons += 1
        if list[mid] == target:
            return comparisons
        elif target > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return comparisons

def binary_search_recursive(list, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if list[mid] == target:
        return mid
    elif target > list[mid]:
        return binary_search_recursive(list, target, mid + 1, end)
    else:
        return binary_search_recursive(list, target, start, mid - 1)

def menu():
    original_numbers = list(range(10000))
    numbers = original_numbers.copy() 

    while True:
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
                numbers = original_numbers.copy()
                print("List has been reset.")
            case "8":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")

menu()
