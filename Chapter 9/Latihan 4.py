import random

def shuffle_string(x, n):
    kata_diacak = []
    i = 0
    while i < n:
        result = "".join(random.sample(x,len(x)))
        if result not in kata_diacak:
            kata_diacak.append(result)
            i+=1
    print (kata_diacak)
shuffle_string("kamu", 3)
shuffle_string("kamu", 4)
shuffle_string("kamu", 5)