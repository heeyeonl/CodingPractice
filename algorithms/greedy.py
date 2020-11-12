# Greedy Algorithm - an algorithmic paradigm that follows the problem solving approach
#                    of making the locally optimal choice at each stage with the hop of
#                    finding a global optimum.
# Pros - simple, easy to implement, run fast O(nlogn) mostly due to sorting
# Cons - often they don't provide a globally optimum solution


# Example 1
# 3 workers and max num of hours of shift should be minimized.
# [6, 5, 2, 3, 5, 7] then it should have 
# worker1(3,6) = 9
# worker2(2,7) = 9
# worker3(5,5,) = 10

A = [6, 5, 2, 3, 5, 7]
A.sort()

max = 0
for i in range(len(A)//2): # it should pair shortest + longest shift
    # print(A[i], A[~i])     # ~i goes to -(i+1) index (tracking from backside)
    temp = A[i] + A[~i]
    if temp > max:
        max = temp

print("minimized total hours that worker should work for is", max, "hours.")