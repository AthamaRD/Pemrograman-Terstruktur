print("=" * 70)
print("NIM".ljust(6), "Nama Mahasiswa".ljust(22),"Tanggal Lahir".ljust(22),"Tempat Lahir")
print("-" * 70)

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
for isi in mhs:
    Split = isi.split(":")
    NIM = Split[0]
    Nama = Split[1]
    Tanggallahir = Split[2]
    TanggallahirSplit = Tanggallahir.split("-")
    Tanggal = TanggallahirSplit[2]
    Bulan = TanggallahirSplit[1]
    Tahun = TanggallahirSplit[0]
    TempatLahir = Split[3]
    print(NIM.ljust(7),Nama.ljust(22),Tanggal,"/",Bulan,"/",Tahun,"/".ljust(7),TempatLahir)
print("-" * 70)