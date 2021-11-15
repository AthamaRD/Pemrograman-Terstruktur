#tahun kabisat
tahun=int(input("Tahun berapa ya sekarang? :"))
#Menguji apakah benar ini merupakan tahun kabisat
if(tahun%400==0):
    print("Ya Tahun ini tahun kabisat nih guys")
elif(tahun%100==0):
    print("Tahun ini bukan tahun kabisat guys")
elif(tahun%4==0):
    print("Ya Tahun ini tahun kabisat nih guys")
else:
    print("Tahun ini bukan tahun kabisat guys")