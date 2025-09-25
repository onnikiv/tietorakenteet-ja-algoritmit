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

        # swapataan head jos data on pienempi
        if data < self._head_node._data:
            
            self._head_node, self._head_node._next = Node(data), current
            
        # muuten aletaan iteroimaan lista läpi
        else:

            while current is not None:
                
                # jos ei ole seuraavaa nodea niin tehdään sellainen halutulla datalla
                if current._next is None:
                    current._next = Node(data)
                    break

                # Kun löydetään väli arvolle
                if current._data < data < current._next._data:
                    new_node = Node(data)
                    new_node._next = current._next
                    current._next = new_node
                    break
                
                # seuraavaan
                current = current._next   

                
                

                
          	
l = Sorted_Doubly_Linked_List()
l.append(1)
l.append(2)
l.append(3)
l.print_list()