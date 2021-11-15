datasayur= ['bayam', 'kangkung', 'wortel', 'selada']
print("Menu :")
print("A. Tambah data Sayur")
print("B. Hapus data Sayur")
print("C. Tampilkan data Sayur")
while True:
    pilihan=input("Masukkan pilihan anda A,B,C,D = ")
    if (pilihan == "A"):
        tambah= input("Masukkan sayuran yang mau ditambahkan: ")
        datasayur.append(tambah)
        print("Data Sayuran =", datasayur)
    elif(pilihan == "B"):
        hapus=  input("Masukkan sayuran yang mau dihapus: ")
        if hapus in datasayur:
            datasayur.remove(hapus)
            print("Data Sayuran =", datasayur)
        else:
            print("Data Sayuran tidak dapat ditemukan")
    elif(pilihan == "C"):
        print("Data Sayuran =", datasayur)
        lagi= input("ingin melakukan perubahan(y/n)? ")
        if (lagi == "y"):
            continue
        elif (lagi == "n"):
            break