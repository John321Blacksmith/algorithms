"""
Binary search is an algorithm which
performs searching an item over a
sorted array, dividing it by half
each time the item is not found.
"""


def b_search(array: list, item) -> int:
    """
    :array: list
    :item: any
    
    :returns: <int> Index of the found item, othervice, None
    Time complexity: O(log2(n))
    """
    first = 0
    last = len(array) - 1
    
    while first <= last:
        middle = (first + last) // 2
        guess = array[middle]
    
        if guess < item:
            first = middle + 1
        elif guess > item:
            last = middle - 1
        else:
            return middle
        