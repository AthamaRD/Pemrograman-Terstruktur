buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

print("Data Buah")
for a,b in buah.items():
    print("-", a, "=",b)
print("Menu: ")
print("A. Tambah data Buah")
print("B. Beli Buah")
print("selesai")
while True:
    pilihan= input("Masukkan pilihan Anda(A/B/selesai) = ")
    if(pilihan == "A"):
        while True:
            tambah= str(input("Masukkan nama buah yang ingin didata = "))
            if tambah in buah:
                print("Nama buah sudah ada")
                continue
            else:
                hargabaru= int(input("Masukkan harga buah = "))
                buah.update({tambah:hargabaru})
                tambahlagi= str(input("Ada tambahan lagi(y/n)? "))
                if(tambahlagi == "y"):
                    continue
                elif(tambahlagi == "n"):
                    print("Data Buah")
                    for a,b in buah.items():
                        print("-", a, "=", b)
                    break
        continue
    elif(pilihan == "B"):
        totalharga = 0
        while True:
            namabuah= str(input("Nama buah yang akan dibeli = "))
            if namabuah in buah:
                jumlah= float(input("Berapa Kilogram =  "))
                total= jumlah * buah[namabuah]
                totalharga+= total
                lagi= str(input("Ada tambahan lagi(y/n)? "))
                if (lagi == "y"):
                    continue
                elif (lagi == "n"):
                    print("Total harga = ", totalharga)
                    break
            else:
                print("Buah tidak tersedia")
    elif (pilihan == "selesai"):
        break