nums=[5, 10, 15, 20,3,5,6,7,100,8,99,44,33,212,33,55,22,11,9,8,7,6,5,4,3,2,1]
n = len(nums)
for i in range(n):
    if i not in nums:
        print(i)
        
        
# All numbers missing from 1 to max (works with duplicates)        

present = set(nums)
missing = [n for n in range(1, max(nums) + 1) if n not in present]

print(missing)       
print(len(missing))



n = len(nums)
freq = {}
for i in range(0,n+1):
    freq[i] = 0 
    
              