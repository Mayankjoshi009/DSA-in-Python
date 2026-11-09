#Implementing Linear Search

nums = [5, 10, 15, 20, 3, 5, 6,23,45,78,79,666,77,7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1,8,9,0,8,7,8]
print("The list of numbers is:", nums)
def linear_search(k):
    n = len(nums)
    for i in range(n):
        if nums[i] == k:
            print(f"The {k} is found at index: {i}")
            break
    else:
        print(f"The {k} is not found in the list.")
        
k = int(input("Enter the number to search in the list:"))        
linear_search(k)                