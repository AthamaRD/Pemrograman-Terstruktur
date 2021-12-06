myfile = open('textangka.txt', 'r')
list = []
baca = myfile.readlines()
hasil = []

for i in range (len(baca)) :
    split = baca[i].split('|')
    isi = [int(split[0]), int(split[1].replace('\n',''))]
    hasil += [isi]

newfile = open('hasiljumlah.txt', 'w')

for i in range(len(hasil)):
    jumlah = sum(hasil[i])
    newfile.write(str(jumlah) + '\n')

myfile.close()
newfile.close()