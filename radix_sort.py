"""Algorithms and Data Structures 1 AI - Sorting (Radix Sort)."""

from dataclasses import dataclass, field
import itertools

def get_num_digits(num: int, base: int = 10) -> int:
    """Returns the number of digits of `num` in `base` base."""
    if base <= 1:
        raise ValueError("The base of a number must be at least 2.")
    
    num_digits = 1
    while base**num_digits <= num:
        num_digits += 1
    return num_digits

def merge(lists: list[list[int]]) -> list[int]:
    """Merges multiple lists into a single list by concatenating one after another."""
    # Note: This operation is also sometimes called 'flattening' or 'chaining'.
    return list(itertools.chain.from_iterable(lists))


def get_digit(num: int, digit: int, base: int = 10) -> int:
    """Converts the given number into `base` and returns the `digit`'th digit from the right.

    Args:
        num (int): The number to get the digit from.
        digit (int): What digit to get.
        base (int, optional): The base of `num`. Defaults to 10.

    Raises:
        TypeError: If `num`, `digit` or `base` are not integers.
        ValueError: If `num < 0` or `base < 2`.
        IndexError: If `digit < 0`.
        
    Returns:
        int: A number between [0, base - 1]. The `digit`'th digit from the right.

    Examples:
        `get_digit(123, 0) == 3`
        `get_digit(1018, 1, 16) == 15       # Note that 1018 == 0x3FA and 0xF == 15`
    """
    #Veryfying if the data types are valid
    if not isinstance(num, int) or not isinstance(digit, int) or not isinstance(base, int):
        raise TypeError("num, digit and base should be integers")
    #Veryfying the domain values
    if num < 0:
        raise ValueError("{num} is not non-negative")
    if base < 2:
        raise ValueError("{base} should be at least 2)")
    if digit < 0:
        raise IndexError("{digit} should be non-negative")
    #Getting the digit 
    return (num // (base ** digit)) % base


@dataclass
class RadixSortResult:
    """The return type of `radix_sort`
    
    Attributes:
        sorted_array (list[int]): The sorted array.
        bucket_list_history (list[list[list[int]]]):
              |-------- list of bucket lists (length should be the max number of digits)
              |    |------------------------- list of buckets (length should be `base`)
              |    |    |------------------------------------- list of elements in one bucket
              v    v    v
            list[list[list[int]]]
    """

    sorted_array: list[int] = field(default_factory=list)
    bucket_list_history: list[list[list[int]]] = field(default_factory=list)

    def add_bucket_list_to_history(self, bucket_list: list[list[int]]):
        """Copy and add the given bucket_list to the bucket_list_history."""
        self.bucket_list_history.append(bucket_list.copy())

def radix_sort(array: list[int], base: int = 10) -> RadixSortResult:
    """Sorts the given array of non-negative integers in ascending order using radix sort.

    Args:
        array (list[int]): An array of non-negative integers.
        base (int, optional): The base ('m' in the lecture slides) of the radix sort. \
            This is also the number of buckets that are used. Defaults to 10.

    Raises:
        TypeError: If array is not a list or base/any element in array are not integers.
        ValueError: If `base < 2` or any value in `array[i] < 0`.

    Returns:
        RadixSortResult: A dataclass containing the sorted array as well as a history of the bucket lists as they were during the sorting process.
    """
    result = RadixSortResult()
    # TODO: implement
    # Use a list of lists to store the buckets and their content
    # At the end of every sorting iteration (when all list elements are assigned to buckets)
    # call result.add_bucket_list_to_history(bucket_list)
    # At the end of sorting make sure to assign the sorted array to result.sorted_array.

    #My code is here:
    #Veryfying the data types
    if type(array) is not list:
        raise TypeError("array is not a list")
    if type(base) is not int:
        raise TypeError("base should be an integer")
    if base < 2:
        raise ValueError("base should be at least 2")
    
    for item in array:
        if type(item) is not int:
            raise TypeError("all element should be integers")
        if item < 0:
            raise ValueError("all items should be positive")
    
    #If the array is empty
    if not array:
        result.sorted_array = array
        return result
    #Looking for the max value in the array and check the number of digits
    max_num = max(array)
    max_digits = get_num_digits(max_num, base)
    #Sorting in the incrementing order of digits
    for digit_index in range(max_digits):
        #The number of buckets = to the number of digits in the base 
        bucket_list = [[] for i in range(base)]
        #Assigning the elements to the buckets 
        for num in array:
            digit = get_digit(num, digit_index, base)
            bucket_list[digit].append(num)
        #Saving the bucket list
        result.add_bucket_list_to_history(bucket_list)
        #Merging the buckets to get the new array
        array = merge(bucket_list)
    result.sorted_array = array


    # First implement this function just using base 10.
    # then extent the function `get_digit` to work with other bases than just 10 and
    # use it to extend this function
    # Note that the base for RadixSort is equivalent to the number of buckets
    return result