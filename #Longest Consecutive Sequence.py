#Longest Consecutive Sequence

nums=[100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9,301,302,303]

n = len(nums)
max_count = 0
for i in range(n):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num += 1
    max_count = max(max_count, count)
    
print("The longest consecutive sequence has a length of:", max_count)

#TC: O(n^2) in worst case, where n is the number of elements in the input list. This is because for each element, we may have to check for the presence of consecutive numbers in the list, which takes O(n) time.
#SC: O(1) as we are using a constant amount of extra space.

#Better Approach:
print("\nBetter Approach")    

last_smallest = float('-inf')
count = 0
longest = 0