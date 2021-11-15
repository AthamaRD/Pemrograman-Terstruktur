buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

namabuah=str(input("Nama buah yang akan dibeli = "))
a= namabuah in buah
r=True
if a:
    while (r==True):
        jumlah=float(input("Berapa Kilogram  : "))
        harga= buah.get(namabuah,0)
        Total=jumlah*harga
        print("--------------------------------")
        print('Total                      = ',Total)
        break
else:
    print("Buah tidak tersedia")