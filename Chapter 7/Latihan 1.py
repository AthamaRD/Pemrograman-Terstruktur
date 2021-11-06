try:
    Namafile = input("Masukkan file: ")
    file = open(Namafile, "r")
    print(file.read())
except FileNotFoundError:
    print("File tidak bisa ditemukan")