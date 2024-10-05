def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        # Track if any swaps happen; if not, the list is sorted
        swapped = False
        print(i)
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(arr)
        # If no swaps occurred, the list is sorted
        if not swapped:
            break
    return arr

# Example usage: 
unsorted_list = [5,4,3,2,1]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)