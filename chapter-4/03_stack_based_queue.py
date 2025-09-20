class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = []
        self._OutboundStack = []

        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.insert(0, data)
        self._size += 1


    def dequeue(self):
        
        if self._size == 0:
            return 
            
        else:
            self._size -= 1
            return self._InboundStack.pop()



	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)