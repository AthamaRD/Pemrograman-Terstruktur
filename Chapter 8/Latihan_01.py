urut = []
banyak = int(input('Berapa banyak angka yang mau diinput?: '))

for i in range(banyak):
    angka = int(input('Masukkan angka: '))
    urut.append(angka)

urut.sort(reverse=True)
print(urut)