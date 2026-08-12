class LinkedList:

    class Node:

        def __init__(self, data, next_node = None) -> None:
            self._data = data
            self._next = next_node

        def data(self) -> Any:
            return self._data
    
    def __init__(self):
        self._head = None
        self._size = 0

    
    def get(self, index: int) -> int:

        if index < 0:
            return -1

        current = self._head
        current_index = 0

        while current_index < index and current is not None:
            current = current._next
            current_index += 1

        if current is None:
            return -1

        return current._data
        

    def insertHead(self, val: int) -> None:

        old_head = self._head
        self._head = LinkedList.Node(val, old_head)
        self._size += 1
        

    def insertTail(self, val: int) -> None:

        current = self._head
        new_node = LinkedList.Node(val)

        if current is None:
            self._head = new_node
        else:
            while current._next is not None:
                current = current._next
            current._next = new_node
        self._size += 1
        

    def remove(self, index: int) -> bool:

        if index < 0 or index >= self._size:
            return False
        if index == 0:
            self._head = self._head._next
            self._size -= 1
            return True

        current = self._head
        current_index = 0
        previous = None

        while current_index < index:
            previous = current
            current = current._next
            current_index += 1
        previous._next = current._next
        self._size -= 1
        return True

    def getValues(self) -> List[int]:

        values = [0] * self._size
        current_index = 0

        current = self._head
        while current is not None:
            values[current_index] = current._data
            current = current._next
            current_index += 1
        return values
        
