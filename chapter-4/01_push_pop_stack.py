class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        self._top = Node(data, self._top)
        self._size += 1
        


        

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        # jos tyhjä
        if self._top is None:
            return None
   
        data = self._top.data
        # ylikirjotetaan seuraavilla arvoilla eli pinon alimmaisilla
        self._top = self._top.next
        self._size -= 1
        return data

    def __repr__(self):
        nodes = []
        current = self._top
        
        while current:
            nodes.append(str(current.data))
            current = current.next
        
        if self._size == 1:
            return f"<Stack ({self._size} element): [{", ".join(nodes)}]>"
        return f"<Stack ({self._size} elements): [{", ".join(nodes)}]>"
        
