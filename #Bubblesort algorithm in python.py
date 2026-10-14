#Bubblesort algorithm in python

num=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]
print("Before sorting:", num)
#Ascending order

n = len(num)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

print("After sorting in ascending order:", num)

#Decending order

n = len(num)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j] < num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

print("After sorting in descending order:", num)

# Time Complexity: O(n^2) in the worst case
# Space Complexity: O(1) as it is an in-place sorting algorithm