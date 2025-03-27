from typing import List  # For type hinting

# Function to find all unique pairs that sum to the target
def twoSumAll(nums: List[int], target: int) -> List[List[int]]:
    result = []  # List to store valid pairs
    seen = {}  # Dictionary to track indices of numbers already seen
    used_indices = set()  # Set to track used indices

    # Loop through the list of numbers
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement to reach target

        if complement in seen:  # Check if the complement has been seen
            for j in seen[complement]:  # Loop through indices of complement
                if j not in used_indices:  # Ensure the complement's index isn't used
                    result.append([j, i])  # Add valid pair
                    used_indices.add(j)  # Mark complement's index as used
                    used_indices.add(i)  # Mark current index as used
                    break
        
        # Add current number and its index to seen
        if num in seen:
            seen[num].append(i)
        else:
            seen[num] = [i]
    
    # Return a message if no pairs are found
    if not result:
        return "No valid pairs found."

    return result  # Return list of valid pairs

# Get user input for numbers
nums = []
while True:
    num = input("Add a number to the 'nums' list, or leave it empty to finish: ")
    if num == '':
        break
    nums.append(int(num))  # Add the number to the list
    
# Get target sum
target = int(input("Choose a target: "))

# Print the result of the function
print(twoSumAll(nums, target))
