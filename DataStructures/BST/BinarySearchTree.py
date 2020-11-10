def search(arr, target):  # target is value we are looking for
    left = 0
    right = len(arr) - 1

    while left <= right:
      mid = (left + right) // 2 # round down
      if arr[mid] == target:  # if value == target, return index num(mid)
        return mid
      elif target < arr[mid]: # when the target is less than mid value
        right = mid - 1 
      else:
        left = mid + 1    # when ethe target is bigger than mid value
    return -1
    
arr1 = [1, 2, 3, 4, 5, 6, 7]
assert search(arr1, 11) == -1
assert search(arr1, 5) == 4
assert search(arr1, 3) == 2

arr2 = [-3, -1, 0, 5, 8, 13]
assert search(arr2, -1) == 1
assert search(arr2, 0) == 2
assert search(arr2, -5) == -1
assert search(arr2, 14) == -1