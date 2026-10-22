#Chech if array is Sorted
nums=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]
def is_sorted(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True




print(is_sorted(nums))
        