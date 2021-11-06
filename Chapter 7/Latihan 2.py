try:
    Nama_file = input('Masukkan file: ')
    file = open(Nama_file,'r')
    
    while True: 
        file = open(Nama_file,'a')
        data = input('Data yang mau ditambahkan: ')
        file.write(data)
        file.close()
        cek = input('Mau lagi (y/n)?: ')
        if cek == 'y' or cek == 'Y':
            True
        elif cek == 'n' or cek == 'N':
            file = open(Nama_file,'r')
            print('Isi File ',Nama_file)
            print()
            print(file.read())
            break
        else:
            print('pilihan tidak ada')
            break
        
except FileNotFoundError:
    print('File tak ditemukan / salah penulisan')