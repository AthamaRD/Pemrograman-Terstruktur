def dataStat(x):
    r= []
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    r.extend([a,b,c])
    return(a,b,c)
#menginput list
n= int(input('jumlah bilangan yang dimasukkan: '))
a= []
i= 0
for i in range (n):
    ab= int(input('Masukkan bilangan: '))
    a.append(ab)
print(dataStat(a))