# 10.4 Sorted Search, No Size
#   You are given an array-like data structure Listy which lacks a size method.
#   It does, however, have an elementAt(i) method that returns the element at index i in O(1) time.
#   If i is beyond the bounds of the data structure, it returns -1.
#   (For this reason, the data structure only supports positive integers.)
#   Given a Listy which contains sorted, positive integers,
#   find the index at which an element x occurs. If x ooccurs multiple times,
#   you may return any index. 
#   Hints: #320, #337, #348
#
# Note:
#   We cannot use original BST because we don't know right, 
#   but we can increase right exponentially [O(logn)].

class Listy(object):
    def __init__(self, arr):
        self.arr = arr
    def elementAt(self, i):
        if i > len(self.arr):
            return -1
        else:
            return self.arr[i]

def searchListy(list, value):
    i = 1
    while list.elementAt(i) != -1 and list.elementAt(i) < value: # why not <= with value?
        i *= 2 # O(logn)
    return binary_search(list, value, i // 2, i)

def binary_search(list, value, left, right):
    while left <= right:
        mid = (left + right) // 2 # should not be float. use //
        mid_val = list.elementAt(mid)
        if value == mid_val:
            return mid
        elif value < mid_val or mid_val == -1: # out of range
            right = mid - 1
        elif value > mid_val:
            left = mid + 1
        else:
            return None


list = Listy([-22, -11, 11, 22, 33, 44, 55, 66, 77, 88, 99])
assert(searchListy(list, 25)) == None
assert(searchListy(list, -22)) == 0
assert(searchListy(list, 11)) == 2
assert(searchListy(list, 22)) == 3
assert(searchListy(list, 77)) == 8
