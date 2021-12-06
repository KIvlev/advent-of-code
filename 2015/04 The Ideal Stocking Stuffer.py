import hashlib 

def find_hash(hash_string):
    seed = "iwrupvqb"
    size = len(hash_string)
    i = 0
    while True:
        h = hashlib.md5((seed + str(i)).encode()).hexdigest()
        if h[:size] == hash_string:
            print(i)
            return
        i += 1

find_hash('00000')
find_hash('000000')