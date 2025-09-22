
        
        
def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """

    for start in range(len(array)//2-1, -1, -1):
        sift_down(array, start, len(array)-1)

    end = len(array)-1

    while end > 0:

        array[0], array[end] = array[end], array[0]

        end -= 1

        sift_down(array, 0, end)

                
        
    
            
        
      
    
array = [6, 8, 5, 1, 2]
heap_sort(array)
print(array)