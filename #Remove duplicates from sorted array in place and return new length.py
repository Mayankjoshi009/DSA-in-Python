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
print("The new length of the array is:", j)        

