def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the pivot (middle element)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right sub-arrays
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Combine the sorted left sub-array, the pivot, and the sorted right sub-array
    return sorted_left + middle + sorted_right

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
