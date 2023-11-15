def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the array


# he time complexity of the binary search algorithm is O(log n), 
# where "n" is the number of elements in the sorted array being searched. 
# This means that the time it takes to perform a binary search grows logarithmically with the size of the input data.