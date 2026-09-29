#reverse a array using recusion


num=[5,7,8,6,3,9,8,5,2,7,4,1,5,7]
def func(num,left,right):
    if left >=right:
        return
    num[left], num[right] = num[right], num[left]
    func(num, left + 1, right - 1)
print(func(num,0,len(num)-1))
print(num)


#1. Reverse number using while loop
def revNum(num, left, right):
  while left <= right:
    num[left], num[right] = num[right], num[left]
    left += 1
    right -= 1
  return num

num =[5,7,8,6,3,9,8,5,2,7,4,1,5,7]
print(revNum(num, left=0, right=len(num)-1))

#2. Keep first and last 2 number as it is, and reverse middle numbers
def revNum(num, left, right):
  if left >= right:
    return num
  num[left], num[right] = num[right], num[left]
  return revNum(num, left + 1, right - 1)  

num =[5,7,8,6,3,9,8,5,2,7,4,1,5,7]
print(revNum(num, left=2, right=len(num)-2))


#TC(O)=(0)N/2==(O)N
#SC(O)=(O)N/2==(O)N









    

      

