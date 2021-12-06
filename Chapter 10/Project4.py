import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

cari = input("Masukkan NIM Dicari : ")
myFile = open(path + "/text2biodata.txt", 'r')
hasil = False


for data in myFile:
    data_copy = data.split("|").copy()
    nim = data.split("|")[0]
    if (nim == cari):
        hasil = data_copy
        break

if (hasil):
    print("Data Mahasiswa")
    print("NIM : " + hasil[0])
    print("Nama : " + hasil[1])
    print("Alamat : " + hasil[2])
else:
    print("Data Tidak Ditemukan")