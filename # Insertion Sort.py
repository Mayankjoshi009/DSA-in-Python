# Insertion Sort

num=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]
print("Before sorting:", num)  
#Ascending Order

n=len(num)
for i in range(1,n):
    key=num[i]
    j=i-1
    while j>=0 and key<num[j]:
        num[j+1]=num[j]
        j=j-1
    num[j+1]=key   
print("After sorting in ascending order:", num) 

# Decending Order

n=len(num)
for i in range(1,n):
    key=num[i]
    j=i-1
    while j>=0 and key>num[j]:
        num[j+1]=num[j]
        j=j-1
    num[j+1]=key    

print("After sorting in descending order:", num) 