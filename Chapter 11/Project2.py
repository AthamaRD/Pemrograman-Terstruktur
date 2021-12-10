from datetime import *
alldata = []
myfile = open('dataperpustakaan.txt', 'w+')
lagi = 'y'


def inputmember():
    kodemember = input('masukkan kode member\t:')
    namamember = input('masukkan nama member\t:')
    bukumember = input('masukkan nama buku\t\t:')
    tgl = datetime.date(datetime.now())
    back = tgl + timedelta(days=7)
    dataplus = [kodemember, namamember, bukumember, str(tgl), str(back)]
    alldata.append(dataplus)
    global lagi
    lagi = input("input lagi(y/n)\t\t:")
    print()

while lagi == 'y':
    inputmember()
else:
    for i in range(len(alldata)):
        myfile.write('|'.join(alldata[i])+"\n")
    myfile.close()