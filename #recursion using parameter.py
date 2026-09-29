#recursion using parameter
# def func(n,m):
#     if n==0:
#         return
#     print(m)
#     func(n-1,m)
# func(5, 100)    


# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)

# a= int(input("Enter the starting number: "))
# b= int(input("Enter the ending number: "))
# func(a,b)



# 

# def func(n):
#     if n==0:
#         return
#     func(n-1)
#     print(n)
    

# a= int(input("Enter the number: "))
# func(a)


def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,4)       



# def func(n):
#     if n==1:
#         return 1
#     return n + func(n-1)
# func(5)