#hashing in python
# n =[5,3,4,4,5,5,2,2,1,2,7,8,9,10,]
# m=[10,9,8,7,6,5,4,3,2,1]
# for num in m:
#     count=0
#     for x in n:
#         if num==x:
#             count+=1
#     print(f"{num} occurs {count} times in the list n.")


# hash_list=[0]*11  # Index 0 won't be used, indices 1-10 will be used
# for num in n:
#     hash_list[num]+=1
# for num in m:
#     if num<1 or num>10:
#         print(f"{num} is out of range.") 
#     else:
#         print(f"{num} occurs {hash_list[num]} times.")


# n = [10, 3, 6, 10, 2, 5, 3, 8, 6, 10, 4, 2, 5, 8, 3, 10, 1]

# m = [10, 6, 3, 7, 2, 5, 1, 9, 4, 8]

# hash_list =[0]*11
# for num in n:
#    hash_list[num]+=1
# for num in m:
#     if num<1 or num>10:
#      print(f"{num} is out of range.")
#     else:
#          print(f"{num} occurs {hash_list[num]} times.")
         
# freq_dict = {}   

# for num in n:
#     freq_dict[num] = freq_dict.get(num, 0) + 1

# for num in m:
#     if num in freq_dict:
#         print(f"{num} occurs {freq_dict[num]} times.")
#     else:
#         print(f"{num} is out of range.")
        

n = "mississippi"

m = "mispabc"

hash_list = [0]*27                          
for char in n:
    ascii_value = ord(char)
    index =ascii_value -97
    hash_list[index]+=1
for char in m:
    ascii_value = ord(char)
    index =ascii_value -97
    print(f"{char} occurs {hash_list[index]} times.")
    
        

