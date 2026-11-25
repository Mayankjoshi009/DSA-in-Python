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
print("Better Approach")    



last_smallest = float('-inf')
count = 0
longest = 0
nums.sort()
for i in range(n):
    num = nums[i]
    if num-1 == last_smallest:
        count += 1  
        last_smallest = num
    elif num != last_smallest:
        count = 1
        last_smallest = num
    longest = max(longest, count)    
print("The longest consecutive sequence has a length of:", longest)

#TC: O(nlogn) due to sorting the input list.
#SC: O(1) as we are using a constant amount of extra space.


#Optimal Approac:

nums = [100, 4, 200, 1,1,2, 3, 2, 5, 6, 7, 8, 9]

num_set=set()
for i in nums:
    num_set.add(i)
longest=0
for num in num_set:
    if num - 1 not in num_set:
        x = num
        count = 1
        while x+1 in num_set:
            count+=1
            x+=1
        longest= max(longest,count)    
print("The longest consecutive sequence has a length",longest)

#TC=O(3N)
#SC=O(N)            