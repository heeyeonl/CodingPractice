# Hash Table:
#   need dictionary ... Key : Value (key is used instead of index)
#   implement - Hash
#             - Insert
#             - Search
#             - Remove 
# !!! It should take O(1) time.
# !!! avoid collisions
# (optional) Uniformly distributed 
#
# Different methods 
# 1. linear probing: if collide, then go to the next empty one
# 2. double-hashing: if collide, then go to next {3rd} one (repeat until empty found)
#
# Helpful YouTube: https://www.youtube.com/watch?v=sfWyugl4JWA


# In hash table, each bucket(index) will have linked list of (key:value) pair.
# Index assigned by ... (first char - 'a') mod arraySize
