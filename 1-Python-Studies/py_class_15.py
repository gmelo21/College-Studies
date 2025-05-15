import random

def quick_sort(sequence, depth=0):
    indent = "    " * depth
    print(f"{indent}quick_sort called with: {sequence}")

    length = len(sequence)
    if length <= 1:
        print(f"{indent}Returning (base case): {sequence}")
        return sequence
    else:
        pivot = sequence.pop()  # Choose pivot (last element)
        print(f"{indent}Chosen pivot: {pivot}")

    items_lower = []
    items_equal = [pivot]
    items_greater = []

    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        elif item > pivot:
            items_greater.append(item)
        else:
            items_equal.append(item)

    print(f"{indent}Items < pivot: {items_lower}")
    print(f"{indent}Items == pivot: {items_equal}")
    print(f"{indent}Items > pivot: {items_greater}")

    sorted_lower = quick_sort(items_lower, depth + 1)
    sorted_greater = quick_sort(items_greater, depth + 1)

    result = sorted_lower + items_equal + sorted_greater
    print(f"{indent}Merged result: {result}")
    return result


def merge_sort(arr, depth=0):
    indent = "    " * depth
    print(f"{indent}merge_sort called with: {arr}")

    if len(arr) <= 1:
        print(f"{indent}Returning (base case): {arr}")
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    merged = []
    i = j = 0
    print(f"{indent}Merging: {left} + {right}")
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    print(f"{indent}Merged result: {merged}")
    return merged


def display_recursive_sort_results(sort_function, input_list):
    list_copy = input_list.copy()
    print(f"\nRunning {sort_function.__name__}:")
    result = sort_function(list_copy)
    print(f"\nSorted list: {result}")


def menu_recursive():
    current_size = 10
    current_list = list(range(1, current_size + 1))
    random.shuffle(current_list)

    while True:
        print("\nRecursive Sort Menu:")
        print("Current list:", current_list)
        print("1. Merge Sort")
        print("2. Quick Sort")
        print("3. Randomize List")
        print("4. Set List Size")
        print("5. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                display_recursive_sort_results(merge_sort, current_list)
            case "2":
                display_recursive_sort_results(quick_sort, current_list)
            case "3":
                random.shuffle(current_list)
                print("List randomized.")
            case "4":
                try:
                    new_size = int(input("Enter new list size: "))
                    if new_size > 0:
                        current_size = new_size
                        current_list = list(range(1, current_size + 1))
                        random.shuffle(current_list)
                        print(f"List size set to {current_size}.")
                    else:
                        print("Size must be positive.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")


menu_recursive()
