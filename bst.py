"""Algorithms and Data Structures 1 AI - Binary Search Trees."""

import contextlib
from dataclasses import dataclass, field
from typing import Any, Iterable, Iterator, MutableMapping, overload, override

@dataclass
class TreeNode:
    """TreeNode helper class.

    Attributes:
        key (int): Key used for sorting the node into a BST.
        value (Any): Whatever data the node shall carry.
        right (TreeNode): Node to the right.
        left (TreeNode): Node to the left.
        parent (TreeNode): Parent node.
    """

    key: int
    value: Any
    _right: "TreeNode | None" = field(default=None, init=False, repr=False)
    _left: "TreeNode | None" = field(default=None, init=False, repr=False)
    _parent: "TreeNode | None" = field(default=None, init=False, repr=False, compare=False)

    @property
    def right(self) -> "TreeNode | None":
        """Return the right child of this node if existing."""
        return self._right
    
    @right.setter
    def right(self, value: "TreeNode | None"):
        """Set the right child of this node."""
        # NOTE: You may want to additionally update the parent field of the current child 
        # and future child accordingly and avoid ever setting 'parent' explicitly.
        self._right = value

    @property
    def left(self) -> "TreeNode | None":
        """Return the left child of this node if existing."""
        return self._left

    @left.setter
    def left(self, value: "TreeNode | None"):
        """Set the left child of this node."""
        # NOTE: You may want to additionally update the parent field of the current child 
        # and future child accordingly and avoid ever setting 'parent' explicitly.
        self._left = value

    @property
    def parent(self) -> "TreeNode | None":
        """Returns the parent of this node or 'None' if this is a root node."""
        return self._parent

    @parent.setter
    def parent(self, value: "TreeNode | None"):
        """Set the parent of this node."""
        # NOTE: *You may delete this setter* and automatically set '_parent' whenever this node
        # is being set as the left/right node of some other node.
        # This could make your life easier, ensuring that 'node.left.parent == node' all the time.
        self._parent = value
     
    def overwrite_parent(self, new_parent: "TreeNode | None"):
        """Force-set the parent of this node."""
        # This method is used in testing to ensure we can provide you a valid tree.
        self._parent = new_parent

    @property
    def depth(self) -> int:
        """Return depth of the node, i.e. the number of parents/grandparents etc.

        Returns:
            int: Depth of node
        """
        #Assign the counter 
        depth_counter = 0
        current_node = self
        #Iterating until the root node is not reached
        while current_node.parent is not None:
            depth_counter += 1
            current_node = current_node.parent
        return depth_counter

    @property
    def is_external(self) -> bool:
        """Return if node is an external node (= leaf)."""
        return self.left is None and self.right is None

    @property
    def is_internal(self) -> bool:
        """Return if node is an internal node."""
        return not self.is_external



class BinarySearchTree(MutableMapping[int, Any]):
    """Binary-Search-Tree implemented for didactic reasons."""

    @overload
    def __init__(self):
        """Initialize BinarySearchTree."""
        ...

    @overload
    def __init__(self, root: "TreeNode", size: int):
        """Initializes a BinarySearchTree already filled with data.

        Used for testing.

        Args:
            root (TreeNode): Root of the BST.
            size (int): Size of the BST.
        """
        ...

    def __init__(self, root: "TreeNode | None" = None, size: "int | None" = None):
        """Initializes a BinarySearchTree."""
        self._root = root
        self._size = size or 0


    def insert(self, key: int, value: Any) -> TreeNode:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is already present in the tree.
        
        Returns:
            TreeNode: The newly inserted node.
        """
        #Checking if the key carries the proper value 
        if not isinstance(key, int):
            raise TypeError("Improper key value type.")
        #Checking if the tree is not fully empty
        #If it is empty create a new node assign it as a root, +1 to the size and return the node
        if self._root is None:
            new_node = TreeNode(key, value)
            self._root = new_node
            self._size += 1
            return new_node
        #If the tree is not empty, we need to find the right place for the new node
        current_node = self._root
        while True:
            #If it is the same key
            if current_node.key == key:
                raise KeyError("key is already in the tree")
            #if key is smaller go left 
            elif key < current_node.key:
                if current_node.left is None:
                    new_node = TreeNode(key, value)
                    current_node.left = new_node
                    new_node.parent = current_node
                    self._size += 1
                    return new_node
                current_node = current_node.left
                #If the key is bigger go right
            else:
                if current_node.right is None:
                    new_node = TreeNode(key, value)
                    current_node.right = new_node
                    new_node.parent = current_node
                    self._size += 1
                    return new_node
                current_node = current_node.right



    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Raises:
            TypeError: If `key` is not an integer.
            KeyError: If `key` is not present in the tree.
        """
        #Veryfication if it is an integer
        if not isinstance(key, int):
            raise TypeError("Key is not an integer")
        #Veryfication if the tree is empty
        if self._root is None:
            raise KeyError("key not found tree is empty")
        #Going through the tree to find the key 
        current_node = self._root
        while current_node is not None:
            #If the key is found
            if current_node.key == key:
                return current_node
            #If the key is smaller, go left
            elif key < current_node.key:
                current_node = current_node.left
            #If the key is bigger, go right 
            else:
                current_node = current_node.right
            #If none of the nodes are not equal, the key is not in there
        raise KeyError("Key is not in the tree")

    def try_find(self, key: int) -> TreeNode | None:
        """Returns the node with the given key or None if that node doesn't exist.

        Raises:
            TypeError: If key is not an integer.
        """
        with contextlib.suppress(KeyError):
            return self.find(key)
        return None
    

    @property
    def size(self) -> int:
        """Return the number of nodes contained in the tree."""
        return self._size
    

    # This is what is called when you do `len(tree)`
    @override
    def __len__(self) -> int:
        """Returns the number of nodes contained in the tree."""
        return self.size


    # This is what gets called when you call e.g. `tree[5]`
    @override
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: The value of the node with the given key.
        """
        return self.find(key).value
    
    @override
    def __contains__(self, key: object) -> bool:
        """Return whether a node with the given key is in this tress."""
        if not isinstance(key, int):
            return False
        return self.try_find(key) is not None

    @override
    def __setitem__(self, key: int, value: Any) -> None:
        """Sets the value of the node with the given key or inserts a new node."""
        node = self.try_find(key)
        if node is None:
            self.insert(key, value)
        else:
            node.value = value
    
    @override
    def __delitem__(self, key: int) -> None:
        """Removes node with the given key, maintaining BST-properties."""
        self.remove(key)

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        # * HINT:
        # * find node
        # * node has 0 children? => remove node by detaching from parent
        # * node has 1 child?    => attach child to parent (instead of the node)
        # * node has 2 children?
        # * => find inorder-successor of node (how to do that?)
        # * => swap/replace node with inorder successor (maybe add a function for that)
        # * => after that our node has guaranteed at most one child (why that?)
        
        #Veryfying if the key is an integer
        if not isinstance(key, int):
            raise TypeError("Key should be an integer")
        #Looking for the node with the help of the previously assigned method find
        node_remove = self.find(key)
        #Method for removing the node with 0 or 1 child
        def _remove_small(node: TreeNode):
            #veryfing if the child exists or not
            child = node.left if node.left is not None else node.right
            #If deleting the root node
            if node.parent is None:
                self._root = child
                if child is not None:
                    child.parent = None
            #If the node is a parent's left child
            elif node == node.parent.left:
                node.parent.left = child 
                if child is not None:
                    child.parent = node.parent
            #If the node is a parent's right child
            else:
                node.parent.right = child
                if child is not None:
                    child.parent = node.parent
        #The node has 2 children
        if node_remove.left is not None and node_remove.right is not None:
            #Find inorder successor (the smallest node in the right subtree)
            inorder_successor = node_remove.right
            #The smallest most similar node is the leftmost node in the right subtree
            while inorder_successor.left is not None:
                inorder_successor = inorder_successor.left
            #Changing the key and value with the successor to finalize the process
            node_remove.key, inorder_successor.key = inorder_successor.key, node_remove.key
            node_remove.value, inorder_successor.value = inorder_successor.value, node_remove.value
            #Remove inorder successor which has the most one child
            _remove_small(inorder_successor)
            #Other is just one or no children 
        else:
            _remove_small(node_remove)
        #Decrementing the size of the tree
        self._size -= 1


    # NOTE: An Iterable is everything where you can write `for _ in <iterable>`
    # you may just return a list, but if you wanna be efficient you compute the order lazily
    # and return a generator instead.
    # Hint: Using a recursive generator with 'yield from' makes this function very easy to implement
    # Generator Tutorial: https://youtu.be/tmeKsb2Fras
    def inorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in inorder."""
        # if you're confused by `Iterable` just do
        # inorder_list: list[TreeNode] = []
        # <fill inorder_list with nodes in-order>
        # return inorder_list
        #Going from left to right, therefore, checking the smallest nodes first and creating the sorted order
        def _indorder_method(node: TreeNode | None) -> Iterable[TreeNode]:
            if node is not None:
                yield from _indorder_method(node.left)
                yield node
                yield from _indorder_method(node.right)
        yield from _indorder_method(self._root)


    def preorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in preorder."""
        # See `inorder` for hints
        #Going from the root to the left and then right 
        def _preorder_method(node: TreeNode | None) -> Iterable[TreeNode]:
            if node is not None:
                yield node
                yield from _preorder_method(node.left)
                yield from _preorder_method(node.right)
        yield from _preorder_method(self._root)

    def postorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in postorder."""
        # See `inorder` for hints
        #Going from left to right and then to the root
        def _postorder_method(node: TreeNode | None) -> Iterable[TreeNode]:
            if node is not None:
                yield from _postorder_method(node.left)
                yield from _postorder_method(node.right)
                yield node
        yield from _postorder_method(self._root)
    # this allows for e.g. `for key in tree` and is required for a mutable mapping
    @override
    def __iter__(self) -> Iterator[int]:
        return iter(node.key for node in self.preorder())

    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        #To perform the check well we need to compare the nodes to only to the parents but to the range, therefore, we assign min and max allowed
        #Assign floats as they have the limits, avoiding additional checks
        def _is_valid_perform(node: "TreeNode | None", min_allowed: float, max_allowed: float) -> bool:
            #None node is valid
            if node is None:
                return True
            #Veryfing the node key within the range
            if not (min_allowed < node.key < max_allowed):
                return False
            #Check the left and right subtree minding the max min 
            return (_is_valid_perform(node.left, min_allowed, node.key) and _is_valid_perform(node.right, node.key, max_allowed))
        #Perfrom the veryification from the root
        return _is_valid_perform(self._root, float("-inf"), float("inf"))


    def return_min_key(self) -> "TreeNode | None":
        """Return the node with the smallest key (None if tree is empty)."""
        #The smallest node is by definition the leftmost one, therefore, going to the left side until None is reached
        #Checking the tree validaty
        if self._root is None:
            raise KeyError("tree is empty")
        current_node = self._root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def return_max_key(self) -> "TreeNode | None":
        """Return the node with the largest key (None if tree is empty)."""
        #Looking for the biggest node is performed by going to the rightmost node, which is therefore, the biggest one in the binary search tree
        #If the tree is empty, it does not exist
        if self._root is None:
            raise KeyError("tree is empty")
        current_node = self._root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    @staticmethod
    def count_comparisons(for_list: "list[int]", key: int) -> "tuple[int, int]":
        """Count how many comparisons are needed to find a specific key in a list vs bst.

        Creates a Binary Search tree, inserts all values from `for_list` and then checks
        how many comparisons are needed to find `key` vs how many comparisons are required when
        just going through the list one element after another. 

        `for_list` must not contain duplicates.

        Args:
            for_list (list[int]): The list to check against and build a BST from.
            key (int): The key to find.

        Returns:
            tuple[int, int]:
                0: The number of comparisons walking through the list.
                1: The number of comparisons used in the bst.
        """
        #Count the comparisons for the list 
        list_comparisons = 0
        for item in for_list:
            list_comparisons += 1
            if item == key:
                break
        #Build the binary search tree and count the comparisons for it
        tree = BinarySearchTree()
        for item in for_list:
            tree.insert(item, item)
        tree_comparisons = 0
        current_node = tree._root
        while current_node is not None:
            tree_comparisons += 1
            #if it is the same one
            if current_node.key == key:
                break
            #if the key is smaller, go left
            tree_comparisons += 1
            if key < current_node.key:
                current_node = current_node.left
            #if the key is bigger, go right
            else:
                current_node = current_node.right
        return (list_comparisons, tree_comparisons)


    @property
    def root(self) -> "TreeNode | None":
        """Returns the root of the Binary Search Tree."""
        return self._root

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self.inorder())})"

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

