# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times, write code to finid an element in the array.
#                          You may assume that the array was originally sorted in increasing order.

# Example
# Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)


# My initial thought:
# Can we just go through from the beginning each items and if it matches.
# Will it not be O(n) because we only go through once?
# Do we need to know what is the pivot of the rotation?
# ====> YES, because version 1 would work fine too, but we are looking for the better solution with faster run time complexity for efficiency.
#       version 1 would take O(n) time, but if we do binary search, it will cut down to O(logn).

# version 1 (slower, O(n))
def search1(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


# Do modified binary search!! ***
# YouTube: https://www.youtube.com/watch?v=oRllj-ObrBU
# version 2 (faster, O(logn))
def search2(target, arr):
    num = len(arr)
    left = 0
    right = num - 1

    if num == 0:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        
        if target <= arr[mid]:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                
        


A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
B = [7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 7
print(search1(target, A))