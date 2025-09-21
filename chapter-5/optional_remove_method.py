class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        if node is None:
            return

        if node._left_child is not None and node._right_child is not None:
            raise ValueError("Cannot detach node with two children")

        child = node._left_child if node._left_child is not None else node._right_child
        parent = node._parent

        if parent is None:
            self._root_node = child
            if child is not None:
                child._parent = None
            return

        if parent._left_child == node:
            parent._left_child = child
        elif parent._right_child == node:
            parent._right_child = child
        if child is not None:
            child._parent = parent

    def _find_successor(self, node):
        """
        Find the successor of a node
        Parameters:
        - 'node': The node for whom a successor has to be found.
        Returns: Returns the succesor node or None if no successor is found.
        """
        current = node._right_child
        while current._left_child:
            current = current._left_child
        return current
    def _replace_node(self, node_to_replace, replacement_node):
        """
        Link the parent and children of the node to be replaced to the replacement node.
        Replacement node and node to be replaced must exist.
        Node to be replaced is not modified.
        If node_to_replace is Root node, then _root_node pointer is updated.
        if BST rules are not fulfilled, an error is thrown.
        """
        # Check nodes exist.
        if node_to_replace is None or replacement_node is None:
            raise(ValueError)
        parent_node = node_to_replace._parent
        # Link the replacement node to the parent
        replacement_node._parent = parent_node # Bottom up
        # If node to replace is Root node, update _root_node pointer.
        if node_to_replace is self._root_node:
            self._root_node = replacement_node # From top to bottom
        # If not, link parent to the replacement on the right or the left
        elif parent_node._left_child is node_to_replace:
        # Replacement is left node
            if replacement_node.data > parent_node.data:
                raise(ValueError)
            parent_node._left_child = replacement_node # From top to bottom
        else:
            # Replacement is right node
            if replacement_node.data < parent_node.data:
                raise(ValueError)
            parent_node._right_child = replacement_node # From top to bottom
        # Link replacement node to child nodes (if any)
        # From parent to child
        replacement_node._left_child = node_to_replace._left_child
        replacement_node._right_child = node_to_replace._right_child
        # From child to parent
        if replacement_node._left_child:
            if replacement_node._left_child.data > replacement_node.data:
                raise(ValueError)
            replacement_node._left_child._parent = replacement_node
        if replacement_node._right_child:
            if replacement_node._right_child.data < replacement_node.data:
                raise(ValueError)
            replacement_node._right_child._parent = replacement_node


    def delete_node(self, data):
        # Find the node to remove
        node_to_remove = self._find(data)
        # if node is not found, return
        if not node_to_remove:
            return
        # If node has only one or no child, just detach the node from the tree,
        # replacing it with one of its childs (if any)
        if node_to_remove._left_child is None or node_to_remove._right_child is None:
            self._detach_node(node_to_remove)
        else:
            # Node to be removed has two children. Find its successor.
            # By definition the successor does not have a left child
            # (because then it would be the actual successor)
            successor_node = self._find_successor(node_to_remove)
            # Detach the successor from the tree
            self._detach_node(successor_node)
            # And replace the node to remove with the successor
            self._replace_node(node_to_remove, successor_node)



	
tree = Tree()
tree.insert(50)
tree.insert(20)
tree.insert(70)
tree.insert(90)
tree.insert(10)
tree.insert(40)
tree.insert(30)
tree.insert(35)
tree.delete_node(20)
print(tree._find(tree._root_node.data))