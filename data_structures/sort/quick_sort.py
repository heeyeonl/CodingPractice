# Quick sort: make any pivot point and divide Sort each item in the list into two sides.
# 1. items less than pivot point
# 2. items greater than pivot point
# After dividing, the pivot will be placed in the middle of the list. 
# ex) [lesser items] + pivot + [greater items]
# Make recursive call until there is no more items to divide.

# Time complexity: O(nlogn) average, O(n^2) worst case
# Memory complexity: O(logn)
# YouTube link: https://www.youtube.com/watch?v=kFeXwkgnQ9U

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1: # no more items to divide
        return sequence
    else:
        items_lesser = []
        items_greater = []
        pivot = sequence.pop() # pop will extract the last element from the list
                               # it doesn't matter which pivot we use. 
        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lesser.append(item)
    return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)

A = [ 8, 9, 2, 1, 5, 7, 6, 3, 3, 9, 1]
print(quick_sort(A))