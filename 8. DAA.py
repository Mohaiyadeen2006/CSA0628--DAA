def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Taking input
arr = list(map(int, input("Enter numbers (space-separated): ").split()))

# Function call
sorted_arr = bubbleSort(arr)

# Output
print("Sorted array:", sorted_arr)
