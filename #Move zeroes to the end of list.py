#Move zeroes to the end of list
nums=[0,9,9,5,9,9,22,35,62,17,18,39,9,0,0,0,9,8,7,6,6,5,4,6,44,89,00,00]
n = len(nums)
temp=[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])

# Append zeros at the end
for i in range(0,len(temp)):
    nums[i]=temp[i]
for i in range(len(temp), n):
    nums[i]=0

print("list after moving zeroes to the end:", nums)

#TC: O(n)
#SC: O(n)

if i == len(nums):
    print(nums)
if len(nums) == 1:
    print(nums)

# Move non-zero values to the front and fill the rest with zeros
j = 0
while i< len(nums):
    if nums[i]==0:
        break
    i +=1
j=i+1

while j < len(nums):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1

print("list after moving zeroes to the end:", nums)

#TC: O(n)
#SC: O(1)
