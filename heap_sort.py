"""Algorithms and Data Structures 1 AI - Sorting (Heap Sort)."""

#Implement downheap method to ensure the heap property
def _downheap(heap: list[int], start_index: int, end_index: int):
    """Goes through the heap starting from the root and transmits the element to the right position when it is against the maxheap property"""
    root = start_index
    #Implement the loop to look for the biggest and transmit the elements
    while True:
        child = root * 2 + 1 #left child
        #If there's no, stop
        if child > end_index:
            break
        #Check the right child and compare to the left one
        if child + 1 <= end_index and heap[child] < heap[child + 1]:
            child += 1 
        #Compare to the root and swap to restore the property
        if heap[root] < heap[child]:
            heap[root], heap[child] = heap[child], heap[root]
            #maintain the indexes and continue
            root = child
        #If both children are smaller, the property is alright
        else:
            break

def make_heap(container: list[int]):
    """Rearranges the elements in `container` in such a way that they form a heap."""
    container_length = len(container)
    if container_length <= 1:
        return
    #Look for the last node that has at least any child
    last_parent = (container_length // 2) - 1
    #Go through the heap starting from the bottom with the downheap method
    for i in range(last_parent, -1, -1):
        _downheap(container, i, container_length - 1)


def pop_heap(heap: list[int], heap_size: int):
    """Shortens the heap by one and moves the biggest element to `heap_size - 1`.

    Rearranges the elements in the heap `heap` in such a way that the part considered the heap
    is shortened by one: The element with the hightest value is moved to `heap_size - 1`.
    """
    if heap_size <= 1:
        return
    last_index = heap_size - 1
    #Swapping the root with the last element
    heap[0], heap[last_index] = heap[last_index], heap[0]
    #Veryifying the property until heap_size - 2
    _downheap(heap, 0, heap_size - 2)

def heap_sort(list_to_sort: list[int]):
    """Sorts the given array using heap sort."""
    list_length = len(list_to_sort)
    if list_length <= 1:
        return
    #Build the heap
    make_heap(list_to_sort)
    #Popping the biggest elements and putting at the end of the list as well as decresing the size
    for current_size in range(list_length, 1, -1):
        pop_heap(list_to_sort, current_size)


def heap_contains(heap: list[int], element: int) -> bool:
    """Returns whether the given element is contained.
    
    Implement this method exploiting the properties of the heap and 
    don't just search through all elements sequentially.
    """
    #Creating the method to easily store the elements 
    def _search_heap(index: int) -> bool:
        #Veryfying the index
        if index >= len(heap):
            return False
        if heap[index] < element:
            return False
        if heap[index] == element:
            return True
        #Perform the serqch for left and right child
        return _search_heap(2 * index + 1) or _search_heap(2 * index + 2)
    #Veryfying the heap
    if not heap:
        return False
    #Call the serach from the root
    return _search_heap(0)
