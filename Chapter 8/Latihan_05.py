def kuadrat(bil):
    l=[]
    for i in range (len(bil)):
        bil[i]**=2
    return bil

n= int(input("Jumlah bilangan yang akan dimasukkan= "))
bil= []
for i in range (n):
    ab= int(input("Masukkan bilangan= "))
    bil.append(ab)
print(kuadrat(bil))