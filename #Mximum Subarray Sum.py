#Maximum Subarray Sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray_sum(nums):
    total = 0
    max_sum = float('-inf')
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            total = total + nums[j]
            max_sum = max(max_sum, total)
    return max_sum

print(max_subarray_sum(nums))

#TC: O(n^2)
#SC: O(1)

#Optimized solution

def max_subarray_sum_optimal(nums):
    max_sum = float('-inf')
    total = 0
    
