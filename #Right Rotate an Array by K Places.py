nums = [5, 10, 15, 20, 3, 5, 6, 7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1,8,9,0,8,7,8]
k = 3
n=len(nums)
rotations=k%n

for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)    
    
    
print("Right rotate array by K place:",nums)    
    