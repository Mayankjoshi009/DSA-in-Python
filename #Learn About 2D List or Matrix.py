#Learn About 2D List or Matrix

nums = [[5, 10, 15, 20, 25, 30],
        [35, 40, 45, 50, 55, 60],
        [65, 70, 75, 80, 85, 90],
        [95, 100, 105, 110, 115, 120],
        [125, 130, 135, 140, 145, 150]]

rows = len(nums)
cols = len(nums[0])

total = 0
for i in range(rows):
    for j in range(cols):
        print(nums[i][j], end="\t")
        total += nums[i][j]
    print()

print("Total:", total)   # 2325

rows = len(nums)
cols=len(nums[0])
total = 0
for i in range(0,rows):
      for j in range(0,cols):
            print(nums[i][j],end=" ")
            total +=nums[i][j]
      print()
      
print("Total of matrix is:",total)



            