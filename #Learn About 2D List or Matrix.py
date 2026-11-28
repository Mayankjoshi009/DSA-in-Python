#Learn About 2D List or Matrix

nums=[[5,10,15],
      [20,25,30],
      [35,40,45]]

rows = len(nums)
cols=len(nums[0])
total = 0
for i in range(0,rows):
      for j in range(0,cols):
            print(nums[i][j],end=" ")
            total +=nums[i][j]
      print()
print("Total of matrix is:",total)            