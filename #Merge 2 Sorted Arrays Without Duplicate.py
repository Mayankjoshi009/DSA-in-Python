#Merge 2 Sorted Arrays Without Duplicates

nums1 = [1,1,1, 3, 5, 7, 9,99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
nums2 = [2,2,2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def merge_sorted_arrays(nums1, nums2):
    merged = []
    n = len(nums1)
    m = len(nums2)
    i, j = 0, 0
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(merged) == 0 or merged[-1] != nums1[i]:
                merged.append(nums1[i])
            i += 1
        else:
            if len(merged) == 0 or merged[-1] != nums2[j]:
                merged.append(nums2[j])
            j += 1
    while i < n:
        if len(merged) == 0 or merged[-1] != nums1[i]:
            merged.append(nums1[i])
        i += 1
    while j < m:
        if len(merged) == 0 or merged[-1] != nums2[j]:
            merged.append(nums2[j])
        j += 1
    print("Merged Array Without Duplicates:", merged)
  
    
merge_sorted_arrays(nums1, nums2)

#TC = O(n + m) where n and m are the lengths of the two input arrays. This is because we are iterating through both arrays once to merge them.  
#SC = O(n + m) in the worst case, where n and m are the lengths of the two input arrays. This is because we are creating a new array to store the merged result, which can have a maximum size of n + m if there are no duplicates. 