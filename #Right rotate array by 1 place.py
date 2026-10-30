#Right rotate array by 1 place

num=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]

n = len(num)
temp = num[n-1]
for i in range(n-2,-1,-1):
    num[i+1]=num[i]
num[0]=temp
print("Right rotate array by 1 place is:",num)

#TC=O(n-1)=O(n)
#SC=O(i)