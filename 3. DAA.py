def sumOfSquares(nums):
    n = len(nums)
    total = 0

    # Generate all subarrays
    for i in range(n):
        distinct_set = set()
        for j in range(i, n):
            distinct_set.add(nums[j])   # add element to set
            count = len(distinct_set)   # distinct count
            total += count * count      # square and add

    return total


# Taking input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))

# Function call
result = sumOfSquares(nums)

# Output
print("Output:", result)
