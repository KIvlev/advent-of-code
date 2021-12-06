# -*- coding: UTF8 -*-
import hashlib 
# initializing string 

def find_hash(size: int):
    seed = "iwrupvqb"
    i = 0
    hash_string = '0' * size
    while True:
        h = hashlib.md5((seed + str(i)).encode()).hexdigest()
        if h[:size] == hash_string:
            print(i)
            return
        i += 1

find_hash(5)
find_hash(6)