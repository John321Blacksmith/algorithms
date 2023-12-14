"""
This algorithm wades through an entire
array and picks up the greatest or smallest
value. After the value has been chosen, it's
retrieved from the array and placed to another
array. And all this works until the last value.
"""


def select_id(array: list) -> int:
    """
    Iterate through the array
    and get an index of the
    smallest list element.
    """
    val_id = 0
    val = array[0]
    for i in range(0, len(array)):
        if array[i] < val:
            val = array[i]
            val_id = i
    
    return val_id


def selection_sort(array: list, sorted_array=[]) -> list:
    """
    Go through an unsorted list
    and retrieve an smallest item
    from the list and place in
    another. 
    """
    unique_elements = [el for el in set(array)]
    if len(unique_elements) == 0:
        return sorted_array
    else:
        sorted_array.append(unique_elements.pop(select_id(unique_elements)))
        return selection_sort(unique_elements, sorted_array)     # recursive case