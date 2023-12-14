"""
This sorting algorithm uses the D&C
technique, finding a pivot, allegedly
middle element and begins to partition
array elements to smaller and greater
than than the pivot.
These two arrays are received by the same
funcion recursively and the process is repeated.
"""


def q_sort(array: list):
    if len(array) <= 2:
        return array    # base case
    else:
        pivot = array[len(array)//2]
        
        smaller = [el for el in array if el < pivot]
        greater = [el for el in array if el > pivot]
        
        return q_sort(smaller) + [pivot] + q_sort(greater)    # recursive case