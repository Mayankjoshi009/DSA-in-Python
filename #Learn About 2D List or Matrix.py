#Learn About 2D List or Matrix

nums = [[5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50],
        [55, 60, 65, 70, 75],
        [80, 85, 90, 95, 100],
        [105, 110, 115, 120, 125]]


rows = len(nums)
cols = len(nums[0])

total = 0
for i in range(rows):
    for j in range(cols):
        print(nums[i][j], end="\t")
        total += nums[i][j]
    print()
      
print("Total of matrix is:",total)

#Upper triangle diagonal


print("Upper triangular matrix:")
upper_sum = 0
for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(nums[i][j], end="\t")
        else:
            print("*", end="\t")
        upper_sum += nums[i][j]      
    print()
print("Upper triangle sum:", upper_sum)
    
#Lower triangle diagonal  
    
    
print("Lower triangular matrix:")
lower_sum = 0
for i in range(rows):
    for j in range(cols):
        if j <= i:
            print(nums[i][j], end="\t")
        else:
            print("*", end="\t")
        lower_sum += nums[i][j]        
    print()
print("Lower triangle sum:", lower_sum)  

#Diagonal element

print("Main diagonal matrix:")
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(nums[i][j], end="\t")
        else:
            print("*", end="\t")
    print() 
diag = [nums[i][i] for i in range(rows)]
print("Diagonal:", diag)         
print("Sum:", sum(diag))

          
print("Anti-diagonal matrix:")


for i in range(rows):
    for j in range(cols):
        if i + j == cols - 1:
            print(nums[i][j], end="\t")
        else:
            print("*", end="\t")
    print()
anti = [nums[i][cols - 1 - i] for i in range(rows)]
print("Anti-diagonal:", anti)    
print("Sum:", sum(anti))          

    
print("Both diagonals together:")      
for i in range(rows):
    for j in range(cols):
        if i == j or i + j == cols - 1:
            print(nums[i][j], end="\t")
        else:
            print("*", end="\t")
    print()