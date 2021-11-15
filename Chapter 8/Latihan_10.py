buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
totalharga=0
while True:
    namabuah=str(input("Nama buah yang akan dibeli  = "))
    if namabuah in buah:
        jumlah=float(input("Berapa Kilogram  = "))
        total=jumlah*buah[namabuah]
        totalharga+=total
        lagi=str(input("Ada tambahan buah lagi(y/n)? "))
        if (lagi == "y"):
            continue
        elif(lagi=="n"):
            print("Total harga =",totalharga)
            break
    else:
        print("Buah tidak tersedia")