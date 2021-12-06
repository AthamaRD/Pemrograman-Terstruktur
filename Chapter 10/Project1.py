myfile = open("text1.txt", "r")
isi = myfile.readlines()

genap= 0
ganjil= 0

print("banyak bilangan genap =", genap)
print("banyak bilangan ganjil =", ganjil)

for i in range (len(isi)) :
    if int(isi[i]) % 2 == 0 :
        genap += 1
    else:
        ganjil += 1

myfile.close()