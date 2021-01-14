# 1.3 URLify
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# Example:
# input:  "Mr John Smith    ", 13
# output: "Mr%20John%20Smith"
# Hints: #53, #118


# The key here is that it has sufficient space at the end ==> working backwards is no problem.
def URLify(str, len):
    print(str)
    print(len)
    url_str = []
    i = int(len) - 1 # conver python string to int
    print(i)
    for c in reversed(str):
        if c == ' ':
            url_str[i-2] = '%'
            url_str[i-1] = '2'
            url_str[i] = '0'
            i = i - 3
        else:
            url_str[i] = c
    # print(i)
    return url_str

if __name__ == "__main__":
    import sys
    print(URLify(sys.argv[1], sys.argv[2]))