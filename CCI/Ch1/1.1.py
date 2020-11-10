# Is Unique: Implement an algorithm to determin if a string has all unique characters. 
# What if you cannot use additional data structures? 
# Hints: #44, #117, #132

def isUnique(string):
    chars = []
    # chras = {}
    for c in string:
        if c in chars:
            return False
        chars.append(c)
        # char[c] = True
    return True

if __name__ == "__main__":
  import sys
  print(isUnique(sys.argv[1]))

