# Quick Sort

nums = [5, 10, 15, 20, 3, 5, 6, 7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original array:", nums)

# Ascending Order
def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


print("Sorted array in ascending order:")
quick_sort(nums, 0, len(nums) - 1)
print(nums)

# Descending Order
num_desc = [5, 10, 15, 20, 3, 5, 6, 7, 100, 8, 99, 44, 33, 212, 33, 55, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original array:", num_desc)


def partition_desc(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort_desc(nums, low, high):
    if low < high:
        pi = partition_desc(nums, low, high)
        quick_sort_desc(nums, low, pi - 1)
        quick_sort_desc(nums, pi + 1, high)


print("Sorted array in descending order:")
quick_sort_desc(num_desc, 0, len(num_desc) - 1)
print(num_desc)