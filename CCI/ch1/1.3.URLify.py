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
def URLify(str, length):
    url_str = [None] * len(str)
    i = int(length) - 1    # i = pointer for str
    j = len(str) - 1       # j = pointer for url_str

    while i != -1:
        if str[i] == ' ':
            url_str[j - 2] = '%'
            url_str[j - 1] = '2'
            url_str[j] = '0'
            j -= 3
            i -= 1
        else:
            url_str[j] = str[i]
            j -= 1
            i -= 1
    return ''.join(url_str)

if __name__ == "__main__":
    import sys
    print(URLify(sys.argv[1], sys.argv[2]))