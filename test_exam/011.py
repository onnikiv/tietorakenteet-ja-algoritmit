class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def next(self):
        return self._next

    def link(self, node):
        self._next = node

    def value(self):
        return self._data


class Singly_Linked_List:
    def __init__(self):
        self._head_node = None

    def append(self, data):
        current = self._head_node
        previous = None
        while current is not None:
            previous = current
            current = current.next()
        new_node = Node(data)
        if previous is None:
            self._head_node = new_node
        else:
            previous.link(new_node)

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def reverse(self):
        
        current = self._head_node
        prev = None
        
        
        while current is not None:
            
            # otetaan seuraava node talteen
            next_node = current._next
            # asetetaan nykyisen pointeri vanhaan
            current._next = prev
            
            prev = current
            current = next_node
            
        self._head_node = prev
            


l = Singly_Linked_List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.reverse()
l.print_list()