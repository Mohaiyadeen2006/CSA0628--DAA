def rob_linear(nums):
    prev = 0
    curr = 0
    
    for money in nums:
        temp = max(curr, prev + money)
        prev = curr
        curr = temp
    
    return curr


def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    # Case 1: exclude last house
    case1 = rob_linear(nums[:-1])
    
    # Case 2: exclude first house
    case2 = rob_linear(nums[1:])
    
    return max(case1, case2)


# Input (single line)
nums = list(map(int, input().split()))

# Output
print(rob(nums))
