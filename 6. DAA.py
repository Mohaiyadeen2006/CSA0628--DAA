def findMaxAfterSort(nums):
    # Check if list is empty
    if len(nums) == 0:
        return "List is empty"

    # Sort the list
    nums.sort()

    # Maximum element will be the last element
    return nums[-1]


# Taking input
user_input = input("Enter numbers (space-separated): ")

# Handling empty input
if user_input.strip() == "":
    nums = []
else:
    nums = list(map(int, user_input.split()))

# Function call
result = findMaxAfterSort(nums)

# Output
print("Output:", result)
