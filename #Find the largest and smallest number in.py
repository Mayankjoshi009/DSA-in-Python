#Find the largest number in an array

#Method 1
nums = [3, 5, 1, 8, 2, 7, 4, 6 , - 10, 0, -5, 15, 20, -2]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
print("Largest number is:", largest)

#Method2 

largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest = nums[i]
print("Largest number is:",largest)        