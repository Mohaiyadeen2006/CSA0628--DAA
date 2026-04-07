def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid  # found, return index
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


# Input array
arr = list(map(int, input("Enter numbers (space-separated): ").split()))
key = int(input("Enter the key to search: "))

# Sort the array first (binary search requires sorted array)
arr.sort()

# Call function
index = binarySearch(arr, key)

# Output
if index != -1:
    print(f"Element {key} is found at position {index}")
else:
    print(f"Element {key} is not found")
