"""Algorithms and Data Structures 1 AI - Queue and Heaps."""

from typing import Collection, Iterator, override


class MinHeap(Collection[int]):
    """A priority queue implementation using a min heap."""

    def __init__(self, raw_heap: list[int] | None = None):
        """Initializes a new min heap, with an optional heap array to use as a basis.

        Args:
            raw_heap (list[int] | None): A already populated heap or None. Used for testing.
        """
        self._heap: list[int] = raw_heap or []

    @property
    def container(self) -> "list[int]":
        """Returns the underlying storage container used in the heap."""
        return self._heap


    def is_empty(self) -> bool:
        """True if the min heap is empty, False otherwise."""
        return len(self._heap) == 0

    #Adding a famous in-class described upheap method for the better implementation and work flow
    def _upheap(self, index: int) -> None:
        """Method to restore the property of the heap therefore moving and element from bottom to top"""
        while index > 0:
            parent_index = (index - 1) // 2
            #Check the main conditions for the minheap and swap if needed
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index
            else:
                break

    #In the same way add the downheap method for moving an element for moving element down
    def _downheap(self, index: int) -> None:
        """Method to keep up the property of the heap and move an element from top to bottom"""
        #Assigning the size variable to iterate through the heap downwards
        size = len(self._heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            #Starting checking the heap property by assigning the smallest to start from the bottom 
            smallest = index 
            #Checking if the children exist and smaller than the smallest adn then going up
            if left_child < size and self._heap[left_child] < self._heap[smallest]:
                smallest = left_child
            if right_child < size and self._heap[right_child] < self._heap[smallest]:
                smallest = right_child
            #If turns out that the child is smaller than the parent, swapping them and updating the index
            if smallest != index:
                self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break

    def push(self, val: int) -> None:
        """Inserts the given value into the min heap."""
        #Primarily adding a new element to the end of the heap 
        self._heap.append(val)
        #Iterating it to the top 
        self._upheap(len(self._heap) - 1)

    def peek(self) -> int:
        """Returns the minimum element of the heap without removing it.
        
        Raises:
            RuntimeError: if the heap is empty.
        """
        #Veryfying if the heap is empty using pre-defined method
        if self.is_empty():
            raise RuntimeError("The heap is empty")
        #In the minheap the min element is always the root 
        return self._heap[0]

    def pop(self) -> int:
        """Removes the minimum element of the heap and returns it.

        Raises:
            RuntimeError: if the heap is empty.
        """
        #Veryfying if the heap is not empty
        if self.is_empty():
            raise RuntimeError("the heap is empty")
        #If there's just one element simply delete it
        if len(self._heap) == 1:
            return self._heap.pop()
        #Saving the min value in order to return it later
        min_value = self._heap[0]
        #Poping the last element and assigning it as a root
        self._heap[0] = self._heap.pop()
        #Performing the pre-difined downheap to restore the property
        self._downheap(0)
        return min_value
            
    @override
    def __len__(self) -> int:
        """The number of elements in the min heap."""
        return len(self._heap)
    
    @override
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.container})"
    
    @override
    def __contains__(self, x: object) -> bool:
        return x in self._heap
    
    @override
    def __iter__(self) -> Iterator[int]:
        return iter(self._heap)
