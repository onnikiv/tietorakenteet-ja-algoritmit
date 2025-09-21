class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        # return len(key) % self.size
        return sum((index+1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.
        
        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start to search from the given position
        current = start

        # While that position is in use, enter the loop
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            
            # If we reach again the given position, that means
            # a whole cycle has been completed and there was no free
            # positions available
            if current == start:
                return None

        # After the loop, current points to a free position
        return current

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupaid and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        

        index = self._find_free_slot(self._hash(key))

        if index == None:
            return
        
        if index <= self.size:
            self.slots[index] = HashItem(key,value)


	
	
h=HashTable()

try:
    for i in range(257):
        h.put(f"key{i}", i)
except MemoryError:
    pass

print(h.slots)