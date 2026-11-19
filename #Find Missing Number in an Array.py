# Find Missing Number in an Array
nums = [23, 7, 40, 12, 3, 18, 7, 29, 35, 1, 14, 22, 9, 31, 5, 18, 26, 38, 11, 2, 33, 16, 27, 8, 19, 36, 4, 30, 12, 21, 25, 10, 37, 6, 34, 15, 28, 3, 24, 20]
# Solution 1

print("Solution 1")

n = len(nums)
for i in range(n):
    if i not in nums:
        print(i)
        

# Solution 2
print("Solution 2")
n = len(nums)
freq = {}
for i in range(0,n+1):
    freq[i] = 0 
    
for i in range(n):
    freq[nums[i]] = 1 
                       
for k,v in freq.items():
    if v == 0:
        print(k)  
        
        
# Optimized Solution 3

print("Optimized Solution 3") 
n = len(nums)
sum_of_nums = sum(nums)

n * (n + 1) // 2 - sum_of_nums
print("Missing number:", n * (n + 1) // 2 - sum_of_nums)

# TC=O(n) and SC=O(1)
        
                                     
# All numbers missing from 1 to max (works with duplicates)        

print("All numbers missing from 1 to max (works with duplicates)")
present = set(nums)
missing = [n for n in range(1, max(nums) + 1) if n not in present]

print("Missing numbers:", missing)       
print("Count of missing numbers:", len(missing))



