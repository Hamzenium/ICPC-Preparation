def insertion_sort(arr):
    # Start from the second element since the first element is already considered sorted.
    for i in range(1, len(arr)):
        # Store the current element to be inserted into the sorted portion.
        current_element = arr[i]
        j = i - 1

        # Move elements of the sorted portion that are greater than the current element
        # one position to the right.
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into its correct position.
        arr[j + 1] = current_element

# Example usage:
my_list = [12, 11,25, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array is:", my_list)
