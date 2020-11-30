# 1.2 Check Permutation: 
#   Given two strings, wrtie a method to decide if one is a
#   permutation of the other
#   Hints: #1, #84, #122, #131
# 
# Notes: 
#       - permutation: one of several possible variants
#       - len(str1) == len(str2)

def isPermutation(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False
    # This sholud work, but sorting costs O(nlogn) time.
    # Using Counter, though, will be O(n) time.
    # Counter essentially creates a list of frequencies.
    # (Imagine a string with 1,000,000,000 characters.)


from collections import Counter
def isPermutation2(str1, str2):
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if c not in counter:
            return False
        counter[c] -= 1
        if counter[c] == 0:
            del counter[c]
    return len(counter) == 0
    

if __name__ == "__main__":
    import sys
    # print(isPermutation(sys.argv[1], sys.argv[2]))
    print(isPermutation2(sys.argv[1], sys.argv[2]))

