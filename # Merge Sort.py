# Merge Sort

num = [5, 10, 15, 20, 3, 5, 6, 7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original array:", num)
# Ascending Order

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge_array(left_sorted, right_sorted)


def merge_array(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


merged_array = merge_sort(num)
print("Ascending order:", merged_array)


# Descending Order

def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort_desc(left_half)
    right_sorted = merge_sort_desc(right_half)
    return merge_array_desc(left_sorted, right_sorted)

def merge_array_desc(left, right):  
    
    merged = []
    i, j = 0, 0
    n,m = len(left), len(right) 

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1  
            
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged   

merged_array_desc = merge_sort_desc(num)
print("Descending order:", merged_array_desc)   

# Time Complexity: O(n log n) in the worst case
# Space Complexity: O(n) due to the temporary arrays used for merging