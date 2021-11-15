a= int(input("Ingin menginputkan berapa mahasiswa?: "))
l= []
i= 0
for i in range(a):
    Nama= input("Masukkan Nama Mahasiswa : ")
    l.append(Nama)
l.sort
r= 0
for r  in range(len(l)):
    print(l[r], "(", len(l[r]), "(karakter)" )
    r += 1