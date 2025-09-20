# viime tehtävästä
class Queue:
    
    def __init__(self):
        self._size = 0
        self._queue = []
        
    def enqueue(self, data):
        self._size += 1
        self._queue.insert(0, data)
        
    def dequeue(self):
        if self._size == 0:
            return
        else:
            self._size -= 1
            return self._queue.pop()
        
    def __repr__(self):
        count = "elements"
        if self._size == 1:
            count = "element"
        return f"<Queue ({self._size} {count}): [{", ".join(self._queue)}]>"

def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:
            if odd_queue._size > 0:
                odd = odd_queue.dequeue()
                pairs.append((num, odd))
            else:
                even_queue.enqueue(num)
        else:
            if even_queue._size > 0:
                even = even_queue.dequeue()
                pairs.append((even, num))
            else:
                odd_queue.enqueue(num)
    return pairs

        


	
print(get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]))