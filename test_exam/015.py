class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None
    def next(self):
        return self._next
    def previous(self):
        return self._previous
    def link_next(self, node):
        self._next = node
    def link_previous(self, node):
        self._previous = node
    def value(self):
        return self._data


class Sorted_Doubly_Linked_List:
    def __init__(self):
        self._head_node = None

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def append(self, data):

        current = self._head_node

        
        # jos lista on tyhjä
        if self._head_node is None:
            self._head_node = Node(data)

        
        
        
        if data < self._head_node._data:
            
            self._head_node, self._head_node._next = Node(data), current
            
        else:

            while current is not None:
                
                if current._next is None:
                    current._next = Node(data)
                    break

                
                if current._data < data < current._next._data:
                    new_node = Node(data)
                    new_node._next = current._next
                    current._next = new_node
                    break
                
                
                current = current._next   

        # Respect the indentation, so the method can be added to the class
    def merge(self, other):
        # Implement the method
        
        a = self._head_node
        b = other._head_node
        
        
        if not a:
            self._head_node = b
            other._head_node = b
            return
        if not b:
            other._head_node = a
            return
        
        # katotaan kummassa listassa eka alkio on pienempi ja asetetaan headiksi
        # napataan seuraava alkio
        if a._data < b._data:
            head = a
            a = a._next
        else:
            head = b
            b = b._next
            
        current = head
        
        
        while a and b:
            if a._data < b._data:
                current._next = a
                a._previous = current
                current = a
                a = a._next
            else:
                current._next = b
                b._previous = current
                current = b
                b = b._next


        if a:
            current._next = a
            a._previous = current
        elif b:
            current._next = b
            b._previous = current


        self._head_node = head
        other._head_node = head
        
           
                
l1 = Sorted_Doubly_Linked_List()
l1.append(9)
l1.append(5)
l1.append(7)
l1.append(1)
l1.append(3)
l2 = Sorted_Doubly_Linked_List()
l2.append(2)
l2.append(8)
l2.append(0)
l2.append(6)
l2.append(4)
l1.merge(l2)
l1.print_list()
l2.print_list()