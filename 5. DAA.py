def findMax(nums):
    maximum = nums[0]   # assume first element is max

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


# Taking input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))

# Function call
result = findMax(nums)

# Output
print("Output:", result)
