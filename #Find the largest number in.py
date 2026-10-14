#Find the largest number in an array

#Method 1
nums = [3, 5, 1, 8, 2, 7, 4, 6 , - 10, 0, -5, 15, 20, -2]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
print("1.Largest number is:", largest)


largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest = nums[i]
print("2.Largest number is:",largest)  


#Method 2


largest = float("-inf")
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest = nums[i]
print("3.Largest number is:",largest)

#TC->O(n)
#SC->O(1)

     