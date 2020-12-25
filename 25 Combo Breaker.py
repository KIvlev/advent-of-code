# -*- coding: UTF8 -*-
import time

def decrypt(key):
    start_time = time.time()
    res = 1
    i = 0
    while res != key:
        i += 1
        res = (res * 7) % 20201227
        if res == key:
            print(i, key)
            break
    print('time: ', time.time() - start_time)
    return i, res

lc, kc = decrypt(9789649)
ld, kd = decrypt(3647239)

res = 1
for i in range(lc):
    res = (res * kd) % 20201227
print(res)

