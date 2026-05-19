"""Algorithms and Data Structures 1 AI - Linked Lists."""

from dataclasses import dataclass
import sys
from typing import Any, Iterator, Sequence, overload, override


@dataclass
class MyListNode:
    value: int
    prev_node: "MyListNode | None" = None
    next_node: "MyListNode | None" = None

class MySortedDoublyLinkedList(Sequence[int]):
    """A base class providing a doubly linked list representation."""

    @overload
    def __init__(self) -> None:
        """Initializes a new SortedDoublyLinkedList."""
        ...

    @overload
    def __init__(self, head: MyListNode, tail: MyListNode, size: int):
        """Initializes a new SortedDoublyLinkedList using predefined `head` and `tail`.

        Used for testing.
        """
        ...

    def __init__(
        self,
        head: "MyListNode | None" = None,
        tail: "MyListNode | None" = None,
        size: int = 0,
    ) -> None:
        self._head = head
        self._tail = tail
        self._size = size

    @override
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    @override
    def __iter__(self) -> Iterator[int]:
        node = self._head
        while node:
            yield node.value
            node = node.next_node

    @override
    def __reversed__(self) -> Iterator[int]:
        node = self._tail
        while node:
            yield node.value
            node = node.prev_node

    @overload
    def __getitem__(self, index: int) -> int:
        ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[int]:
        ...

    @override
    def __getitem__(self, index: int | slice) -> int | Sequence[int]:
        # proper implementation of Sequence interface
        if isinstance(index, slice):
            rv = []
            for idx in range(*index.indices(len(self))):
                rv.append(self[idx])
            return rv
        if isinstance(index, int) and index < 0:
            index = len(self) - index
        return self._get_value(index)

    def _get_value(self, index: int) -> int:
        """Return the value (elem) at position "index" without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            int: Retrieved value.

        Raises:
            IndexError: If the passed index out of range.
        """
        """Check if the index is valid."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} is out of range") 
        """Assigning the current node and checking every element (index) times unless it's reached."""
        current_node = self._head
        for nodes in range(index):
            current_node = current_node.next_node
        return current_node.value


    @override
    def index(self, value: Any, start: int = 0, stop: int = sys.maxsize) -> int:
        """Return the index of the first occurrence of `value` in the list.

        Args:
            val (Any): Value to be searched.
            start (int): A number representing where to start the search.
            stop (int): A number representing where to end the search.

        Raises:
            ValueError: If the given value isn't found.
            
        Returns:
            int: Retrieved index.
        """
        if not isinstance(value, int):
            raise ValueError(f"{value} is not in list.")
        
        current_node = self._head 
        current_index = 0 
        
        """Going through the list unless the value is in the range or the end of the list is reached."""
        while current_node is not None and current_index < stop:
            """Checking if index is valid"""
            if current_index >= start:
                if current_node.value == value:
                    return current_index
                """If current node value is greater than the value we break because the list is sorted and the value will not be found."""
                if current_node.value > value:
                    break 
                """Now implement steps to find the value"""
            current_node = current_node.next_node
            current_index += 1
        raise ValueError(f"{value} is out of the list")
                

        raise NotImplementedError()

    def insert(self, val: int) -> None:
        """Add a new node containing "val" to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            TypeError: If val is not an int.
        """
        """Checking if the value is an integer."""
        if not isinstance(val, int):
            raise TypeError(f"{val} is not an integer.")
        """Creating the new node."""
        the_new_node = MyListNode(val)
        """If the list is empty, new node will become both head and tail."""
        if self._head == None:
            self._head = the_new_node
            self._tail = the_new_node
            self._size += 1
            return
        """If new value is the smalles assign it as a head."""
        if val <= self._head.value:
            the_new_node.next_node = self._head
            self._head.prev_node = the_new_node
            self._head = the_new_node
            self._size += 1 
            return
        """Looking for the insertion place."""
        current_node = self._head
        while current_node is not None and current_node.value < val:
            current_node = current_node.next_node
        """If the current node became None insert it as a tail."""
        if current_node == None:
            the_new_node.prev_node = self._tail
            self._tail.next_node = the_new_node
            self._tail = the_new_node
            """The node with the greater value is found. Insert the new node before it."""
        else:
            previous_node = current_node.prev_node
            previous_node.next_node = the_new_node
            the_new_node.prev_node = previous_node
            the_new_node.next_node = current_node
            current_node.prev_node = the_new_node 
        self._size += 1


    def remove(self, val: int) -> None:
        """Remove the first occurrence of the parameter "val".

        Args:
            val (int): Value to be removed.

        Raises:
            ValueError: If `val` is not present.
        """
        if not isinstance(val, int):
            raise ValueError(f"{val} is not in list.")
        
        """Looking for the node with the proper value."""
        current_node = self._head
        while current_node is not None:
            if current_node.value == val:
                break
            """If the node's value is greater than the one we're looking for, it isn't there."""
            if current_node.value > val:
                current_node = None
                break
            current_node = current_node.next_node
            if current_node is None:
                raise ValueError(f"{val} is not in list.")
            """Removing"""
            """If it is the only node in the list."""
            if self._size == 1:
                self._head = None
                self._tail = None
            #It's the head
            elif current_node == self._head:
                self._head = current_node.next_node
                self._head.prev_node = None 
            #It's the tail
            elif current_node == self._tail:
                self._tail = current_node.prev_node
                self._tail.next_node = None
            #It's in the middle 
            else:
                prev_node = current_node.prev_node
                next_node = current_node.next_node
                prev_node.next_node = next_node
                next_node.prev_node = prev_node

                self._size -= 1

            


    def remove_all(self, val: int) -> int:
        """Remove all occurrences of the parameter "val".

        Args:
            val (int): Value to be removed.

        Returns:
            int: the number of elements removed.
        """
        #Checking if the value is integer 
        if not isinstance(val, int):
            raise ValueError(f"{val} is not integer.")
        """Assign counter of removed elements"""
        removed_counter = 0
        current_node = self._head
        while current_node is not None:
            if current_node.value > val:
                break
            next_node = current_node.next_node
            if current_node.value == val:  
                #The only node in the list 
                if self._size == 1:
                    self._head = None
                    self._tail = None
                #Removing the head
                elif current_node == self._head:
                    self._head = next_node
                    self._head.prev_node = None
                #Removing the tail
                elif current_node == self._tail:
                    self._tail = current_node.prev_node
                    self._tail.next_node = None
                #Removing from the middle
                else:
                    prev_node = current_node.prev_node
                    next_node = current_node.next_node
                    prev_node.next_node = next_node
                    next_node.prev_node = prev_node

                removed_counter += 1
                self._size -= 1
                current_node = next_node
        return removed_counter 
                    

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        current_node = self._head
        """Going through until we have both current and next nodes."""
        while current_node is not None and current_node.next_node is not None:
            """If current and next nodes are the same"""
            if current_node.value == current_node.next_node.value:
                dublicate_node = current_node.next_node
                next_after_dublicate = dublicate_node.next_node
                """Remove the dublicate and connect with the following one."""
                current_node.next_node = next_after_dublicate
                """If after the dublicate there is a node, connect it with the current one."""
                if next_after_dublicate is not None:
                    next_after_dublicate.prev_node = current_node
                """If it was the last element"""
            else:
                self._tail = current_node
            
            self._size -= 1

            """"If the values are different, just move"""
        else:
            current_node = current_node.next_node



    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the "n" highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            TypeError: If the passed value n is not an int.
            ValueError: If the passed value n is out of range.
        """
        """Checking if n is an integer"""
        if not isinstance(n, int):
            raise TypeError(f"{n} is not an integer")
        """Checking the n's range validity"""
        if n <= 0 or n > self._size:
            raise ValueError(f"{n} is out of range")
        
        if n == self._size:
            return
        """Counting the amount of cut values"""
        nodes_to_cut = self._size - n

        current_node = self._head
        """Moving to find a new head"""
        for i in range(nodes_to_cut):
            current_node = current_node.next_node
        """Assign the head and cut all previous nodes"""
        self._head = current_node
        self._head.prev_node = None
        self._size = n


    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next_node
            
            # Checking if it is even
            if current_node.value % 2 == 0:
                if self._size == 1:
                    self._head = None
                    self._tail = None
                elif current_node == self._head:
                    self._head = next_node
                    self._head.prev_node = None
                elif current_node == self._tail:
                    self._tail = current_node.prev_node
                    self._tail.next_node = None
                else:
                    prev_node = current_node.prev_node
                    prev_node.next_node = next_node
                    next_node.prev_node = prev_node
            self._size -= 1
        current_node = next_node

        




    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        current_node = self._head 
        while current_node is not None:
            next_node = current_node.next_node
            #Checking if it is even
            if current_node.value % 2 != 0:
                #It is the only element
                if self._size == 1:
                    self._head = None
                    self._tail = None
                #Removing the tail
                elif current_node == self._tail:
                    self._tail = current_node.prev_node
                    self._tail.next_node = None
                #Removing the head
                elif current_node == self._head:
                    self._head = next_node
                    self._head.prev_node = None
                #Removing from the middle
                else:
                    prev_node = current_node.prev_node
                    next_node = current_node.next_node
                    prev_node.next_node = next_node
                    next_node.prev_node = prev_node
                self._size -= 1
            current_node = next_node



  
