# merge sort uses divide-and-conquer algorithm, meaning it will break down to smaller problems and solve it.
# Since it divdies in half and merge makes it double of its size, its time complexity is O(nlogn). -> we are comparing each one that is n work time.
# It is also recursive.
# merge sort is good for big data because you can save half of the data when you merge sort.

# https://www.youtube.com/watch?v=Nso25TkBsYI&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=4

import sys

def merge_sort(arr):
    merge_sort_2(arr, 0, len(arr)-1) # user calls given one array

def merge_sort_2(arr, first, last):
    if first < last:    # if arr has more than one
        mid = (first + last) // 2     # find the mid index
        merge_sort_2(arr, first, mid)    # left side
        merge_sort_2(arr, mid+1, last)   # right side
        merge(arr, first, mid, last)     # merge

def merge(arr, first, mid, last):
    L = arr[first:mid+1]    # copy the first half of the list
    R = arr[mid+1:last+1]   # copy the last half of the list
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:    # if left first element is smaller than the right first element
            arr[k] = L[i]   # then add left[i] to array
            i += 1          # move pointer to the next element in left
        else:
            arr[k] = R[j]
            j += 1

A = [5,9,1,2,4,8,6,3,7]
print(A)
merge_sort(A)
print(A)    # this is in-place sort so done in original arr.

# sidenote: sort() -> modifies the list in-place
#           sorted() -> new sorted list that is iterable