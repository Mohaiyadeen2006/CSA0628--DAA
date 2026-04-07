def findIntersectionValues(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = 0
    for num in nums1:
        if num in set2:
            answer1 += 1

    answer2 = 0
    for num in nums2:
        if num in set1:
            answer2 += 1

    return [answer1, answer2]


# Taking input from user
nums1 = list(map(int, input("Enter nums1 (space-separated): ").split()))
nums2 = list(map(int, input("Enter nums2 (space-separated): ").split()))

# Calling function
result = findIntersectionValues(nums1, nums2)

# Printing output
print("Output:", result)
