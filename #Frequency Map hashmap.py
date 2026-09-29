#Frequency Map
list = []
n = int(input("How many elements you want to store in list? "))
for i in range(n):
    element = int(input("Enter element: "))
    list.append(element)
hash_map = {}
for i in range(0,n):
    hash_map[list[i]] = hash_map.get(list[i], 0) + 1
print("Frequency Map: ", hash_map)