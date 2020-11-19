# 10.1 Sorted Merge: 
#   You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
#   Write a method to merge B into A in sorted order.



# My initial thought: 
# Since A has large enough buffer to hold B, I can just add B to A and sort it? 
# Or I can just merge sort A and B into A so that space complexity stays the same?
# Merge sort time complexity is O(nlogn).

def merge(A, B):
    index = len(A) - 1  # needs to start from back to add B to A. (already sorted lists, so largest from back)
    indexA = len(A) - len(B) - 1
    indexB = len(B) - 1

    while indexB >= 0:
        if indexA > 0 and A[indexA] > B[indexB]: # when the last elem. of A is greater than the last elem. of B 
            A[index] = A[indexA] # the last elem. of A goes to the last-last of the array when it includes B. -> (A + B) array size
            indexA -= 1
        else:
            A[index] = B[indexB]
            indexB -= 1
        index -= 1
    return A


# These are array generators. (optional)
def fillArrayWithBuffer(numItems, bufferSize):
    arr = []
    for i in range(numItems + bufferSize):
        if i < numItems:
            arr.append(3 * i + 2)
        else:
            arr.append(0)
    return arr

def fillArray(numItems):
    arr = []
    for i in range(numItems):
        arr.append(2 * i + 4)
    return arr

A = fillArrayWithBuffer(5, 8)
B = fillArray(8)
print(A)
print(B)
print(merge(A, B))