

class Queue:
    
    def __init__(self):
        self._size = 0
        self._queue = []

    def enqueue(self,data):
        self._size += 1
        self._queue.insert(0,data)
    
    
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
    

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val)
print(val, queue)