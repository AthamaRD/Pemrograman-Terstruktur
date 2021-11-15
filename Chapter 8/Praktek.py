#Membuat List
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print(a)
print(b)

#Menyisipkan nilai pada list
a.insert(3,10)
b.insert(2,15)
print(a)
print(b)
#Menyisipkan nilai pada indeks terakhir dari list
a.append(4)
b.append(8)
print(a)
print(b)
#Melakukan sorting secara ascending
a.sort()
b.sort()
print(a)
print(b)
#Membuat list yang elemennya merupakan sublist dari list sebelumnya
c= a[0:8]
d= b[2:10]
print(c)
print(d)
#Membuat list yang elemennya merupakan penjumlahan dari list sebelumnya
e=[]
i=0
for i in range(len(c)):
    r=c[i]+d[i]
    e=e+[r]
print (e)
#Mengubah list ke dalam Tuple
liste= tuple(e)
print(liste)
#Mencari nilai max, min, dan jumlah dari tuple
nilaiMax= max(liste)
nilaiMin= min(liste)
jumlah= sum(liste)
print(nilaiMax)
print(nilaiMin)
print(jumlah)
#Membuat variable yang berisi string
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)
#Menentukan karakter huruf apa saja yang terdapat pada string menggunakan set
penyusun=set(myString)
print(penyusun)
#Mengubah string ke list lalu di urutkan
buatlist= list(penyusun)
buatlist.sort()
print(buatlist)