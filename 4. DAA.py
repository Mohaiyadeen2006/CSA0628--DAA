def countPairs(nums, k):
    n = len(nums)
    count = 0

    # check all pairs
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count


# Taking input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))
k = int(input("Enter k: "))

# Function call
result = countPairs(nums, k)

# Output
print("Output:", result)
