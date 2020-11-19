# Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
#
# Q: What is anagram?
# A: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#    typically using all the original letters exactly once.

# My initial thought:
# When string is sorted, anagrams will have exactly same array because it will have 
# same characters in strings if they are anagrams to each others.
# 1. Pop a string from array
# 2. Sort characters in string
# 3. Put it back to array in order

# ===> Since we don't need to build sort function, we can use sorted()
#      Using sorted() and Dictionary {'key':'value'} we will store each word in sorted order.

def groupAnagrams(A):
    dict = {}       # 0. create dictionary
    for word in A:  # 1. sort each word
        key = "".join(sorted(word)) # 2. make key
        if key not in dict:         # 3. if key does not exist, add to dictionary with value
            dict[key] = [word]
        else:       # 4. if exists in dict, then append value to the key
            dict[key].append(word)
        
    result = []
    for word in dict.values(): # 5. Only output words in group of anagrams 
        result.append(word)
    
    return result

        

A = ['fried', 'sadder', 'fired', 'dreads', 'listen', 'silent']
print(groupAnagrams(A))