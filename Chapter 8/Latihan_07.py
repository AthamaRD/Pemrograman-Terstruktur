def Termahal(harga):
    ubah= list(harga.values())
    ubah.sort()
    ubah.reverse()
    r=ubah[0]
    for x,y in harga.items():
        if(y==r):
            return x
    return r 
buah= {"apel": 5000, "jeruk": 8500, "mangga": 7800, "duku": 6500}
print(Termahal(buah))