def sum(*x):
    hasil = 0
    for data in x:
        hasil += data

    return hasil

def avg(*x):
    hasil = sum(*x)
    jumlah = 0
    for data in x:
        jumlah += 1

    return hasil / jumlah

def maks(*x):
    maks = x[0]
    for data in x:
        if maks < data:
            maks = data

    return maks

def min(*x):
    min = x[0]
    for data in x:
        if min > data:
            min = data

    return min