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














def merge_sort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: a single element is already sorted
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    Parameters:
    left (list): The first sorted list.
    right (list): The second sorted list.
    
    Returns:
    list: A merged and sorted list.
    """
    merged = []
    i = j = 0  # Pointers for left and right lists
    
    # Compare elements from left and right lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from left list
    while i < len(left):
        merged.append(left[i])
        i += 1        
    
    # Append any remaining elements from right list
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Example usage:
if __name__ == "__main__":
    # Taking input from the user
    try:
        arr_input = input("Enter the list of values separated by spaces: ")
        arr = list(map(int, arr_input.strip().split()))
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        exit(1)
    
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
