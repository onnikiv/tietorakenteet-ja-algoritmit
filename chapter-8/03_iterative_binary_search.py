def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """

    start = 0 
    end = len(array) - 1

    while start <= end:
        midpoint = start + (end - start + 1) // 2

        if array[midpoint] == value:
            return midpoint
        
        if array[start] != value:
            start += 1
        
        if array[end] != value:
            end -= 1
        
	
	
array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
print(binary_search_iterative(array, 0))
print(binary_search_iterative(array, 98))
print(binary_search_iterative(array, 29))
print(binary_search_iterative(array, 100))
print(binary_search_iterative(array, -1))
print(binary_search_iterative(array, 44))