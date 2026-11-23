#Two Sum

nums = [2, 7, 11, 15,1,2,3,34,5,6,7,8,9,10]

def twoSum(nums, target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return[i,j]
            
print(twoSum(nums,20)) 
                       