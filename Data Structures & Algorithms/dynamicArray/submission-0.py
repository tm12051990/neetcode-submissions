from array import array

class DynamicArray:
    
    def __init__(self, capacity: int):
        """Initialization of an array object"""
        self._capacity = capacity
        self._array = [0] * self._capacity
        self._size = 0

    def get(self, i: int) -> int:
        """Get the element at the given index i"""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[i]


    def set(self, i: int, n: int) -> None:
        """Set the element at index i to n"""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        self._array[i] = n

        return None


    def pushback(self, n: int) -> None:
        """Push the element n to the end of the array"""
        if self._size == self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1


    def popback(self) -> int:
        """Pop and return the last element at the end of the array"""
        element = self._array[self._size - 1]

        self._size -= 1

        return element
 

    def resize(self) -> None:
        """Double the size of the array if full"""
        self._capacity *= 2
        old_array = self._array
        self._array = [0] * self._capacity
        for i in range(self._size):
            self._array[i] = old_array[i]


    def getSize(self) -> int:

        return self._size
        
    
    def getCapacity(self) -> int:

        return self._capacity
