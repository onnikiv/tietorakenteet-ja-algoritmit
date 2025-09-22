class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """

        index = self._size - 1

        
        while index > 0:
            parent_index = (index-1) // 2
            if self._heap[parent_index] > self._heap[index]:

                float_element = self._heap[index]
                parent_element = self._heap[parent_index]
                
                self._heap[index] = parent_element
                self._heap[parent_index] = float_element
                
                index = parent_index
            
            else:
                break
 
	
h = Heap()
h._heap = [3, 6, 5, 9, 7, 8, 2]
h._size = 7
h._float()
print(h._heap)