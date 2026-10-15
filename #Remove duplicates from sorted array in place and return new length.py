#Remove duplicates from sorted array in place and return new length

num=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]

n = len(num)

dict = {}
for i in range(0,n):
    dict[num[i]] = 0
print("The new array is:", list(dict.keys()))    
j = 0
for i in dict:
    num[j] = i
    j += 1
print("1.The new length of the array is:", j) 

#method 2

nums = [5, 10, 15, 20, 3, 5, 6, 7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(num)
if n==1:
    print("2.The new length of the array is:", n)
i = 0
j = i+1
while j<n:
    if num[j] != num[i]:
        i += 1
        nums[i],nums[j] = nums[j],nums[i]
    j += 1
        
print("The new array is:", nums[:i+1])        