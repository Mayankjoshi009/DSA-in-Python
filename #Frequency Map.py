#Frequency Map
list = []
n = int(input("How many elements you want to store in list? "))
for i in range(n):
    element = int(input("Enter element: "))
    list.append(element)
freq_map = {}
for n in list:
    if n in freq_map:
        freq_map[n] += 1
    else:
        freq_map[n] = 1
print("Frequency of each element:", freq_map)