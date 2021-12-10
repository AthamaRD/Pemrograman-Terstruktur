from datetime import *
try:
    datainput = input('masukkan direktori/nama file\t:')
    myfile = open(datainput, 'r')
    teks = myfile.readlines()
    convteks = []
    data = {}

    # memisahkan \n
    for i in teks:
        convteks.append((i.strip()))

    for i in range(len(convteks)):
        splitteks = convteks[i].split('|')
        data[splitteks[0]] = convteks[i]
    # mengambil data dictionary
    kodemember = input('masukkan kode member\t:')
    member = data[kodemember].split('|')
    # data maksimal return dari dictionary ke format date
    x = member[4].split('-')
    batastgl = date(int(x[0]), int(x[1]), int(x[2]))
    # pengembalian dan keterlambatannya member
    mengembalikan = datetime.date(datetime.now())
    terlambat = (mengembalikan - batastgl).days
    if terlambat <= 0:
        melewatihari  = 0
        dendatotal = 0
    else:
        melewatihari = terlambat
        dendatotal = 2000 * terlambat
    # output akhir
    print('\nData Peminjaman Buku\nKode member'.ljust(52), ':', member[0], '\nNama member'.ljust(31), ':', member[1])
    print('Judul buku'.ljust(30), ':', member[2])
    print('tanggal mulai peminjaman'.ljust(30), ':', member[3], '\ntanggal maks peminjaman'.ljust(31), ':', member[4])
    print('tanggal pengembalian'.ljust(30), ':', str(mengembalikan))
    print('Terlambat'.ljust(30), ':', melewatihari, 'Hari')
    print('Denda'.ljust(30), ': Rp', dendatotal)
except FileNotFoundError:
    print('Maaf File Tidak Valid')
except KeyError:
    print('Maaf Member Tidak Valid')