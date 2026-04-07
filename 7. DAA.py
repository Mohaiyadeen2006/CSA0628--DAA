def getUniqueElements(nums):
    unique_list = []
    seen = set()

    for num in nums:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)

    return unique_list


# Taking input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))

# Function call
result = getUniqueElements(nums)

# Output
print("Unique elements:", result)
