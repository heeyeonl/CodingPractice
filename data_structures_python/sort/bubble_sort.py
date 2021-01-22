# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Bubble sort is you compare first two elements
# and swap if left is greater than the right.
# Move to the next element and do the same thing.
# Continue until you cannot swap anymore.

def print_result(num_swap, first, last):
    print('Array is sorted in', num_swap, 'swaps.')
    print('First Element:', first)
    print('Last Element:', last)

def swap(num, arr):
    num_swap = 0
    while True:
        flag_swap = False
        for i in range(num - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                num_swap += 1
                flag_swap = True
        if not flag_swap:
            break
    return print_result(num_swap, arr[0], arr[num-1])


swap(5, [1,2,3,5,4])
swap(3, [6,4,1])

