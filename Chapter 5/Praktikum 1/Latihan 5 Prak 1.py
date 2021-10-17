NameStaff = input("Masukkan Nama Karyawan: ")
CodeStaff = input("Masukkan Kode Karyawan: ")
GolStaff = str(input("Masukkan Golongan     : "))
if (GolStaff == "A") or (GolStaff == "a"):
    GajiPokok = 10000000
    Persen = 2.5

elif (GolStaff == "B") or (GolStaff == "b"):
    GajiPokok = 8500000
    Persen = 2.0

elif (GolStaff == "C") or (GolStaff == "c"):
    GajiPokok = 7000000
    Persen = 1.5

elif (GolStaff == "D") or (GolStaff == "d"):
    GajiPokok = 5500000
    Persen = 1.0

else:
    print("Golongan tidak valid")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("STRUK RINCIAN GAJI KARYAWAN")
print("=============")
print("Nama Karyawan    : " + NameStaff + " (Kode : " + CodeStaff + ")")
print("Golongan         : " + GolStaff)
print("****************************")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Potongan (" + str(Persen) + "%)  : Rp.", int(GajiKotor))
print("|||||||||||||||||||||||||||||||")
print("Gaji Bersih      : Rp.", int(GajiBersih))