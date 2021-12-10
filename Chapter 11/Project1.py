from datetime import *
hariini = datetime.date(datetime.now())
try:
    tglinput = input("Masukkan tanggal yang dicari(YYYY-MM-DD):")
    x = tglinput.split("-")
    tglbaru = date(int(x[0]), int(x[1]), int(x[2]))

    def diffdate(x):
        bedahari = hariini - x
        return bedahari.days

    print('Beda hari dari sekarang & tanggal yang diinput adalah', diffdate(tglbaru), 'hari')
except ValueError:
    print('Maaf Input Tidak Valid')