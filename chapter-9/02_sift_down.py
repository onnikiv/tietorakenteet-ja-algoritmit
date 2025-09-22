def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node
    
    Returns: None
    """
    current_node_index = start
    
    left_child = 2*current_node_index+1
    right_child = 2*current_node_index+2

    big_child = max(array[left_child],array[right_child])
    
    big_child_index = 0
    
    
    
    for i in range(start, end):
        if array[current_node_index] == 1:
            array[end],array[current_node_index] = array[current_node_index],array[end]
        
        if big_child == array[left_child]:
            big_child_index = left_child
        else:
            big_child_index = right_child
        

        if array[current_node_index] < big_child:
            array[current_node_index],array[big_child_index] = big_child, array[current_node_index]
            
        
        
    
    

	
array = [1, 6, 5, 2, 3, 8]
sift_down(array, 0, 4)
print(array)
print([6, 3, 5, 2, 1, 8], " odotettu")