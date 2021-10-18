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

StatMenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

if (StatMenikah == 1):
    Status = "Menikah"
    TunjMenikah = 10 / 100 * GajiPokok
    JmlhAnak = int(input("Masukkan jumlah Anak  : "))
    TunjAnak = 5 / 100 * GajiPokok
    TunjAnak = TunjAnak * JmlhAnak

elif (StatMenikah == 2):
    Status = "Belum Menikah"
    TunjMenikah = 0
    TunjAnak = 0
    JmlhAnak = "-"

else:
    print("Status Menikah Tidak Valid")

GajiKotor = GajiPokok + TunjMenikah + TunjAnak
potongan = Persen / 100 * GajiKotor
GajiBersih = GajiKotor - potongan

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("STRUK RINCIAN GAJI KARYAWAN")
print("===================")
print("Nama Karyawan    : " + NameStaff + " (Kode : " + CodeStaff + ")")
print("Golongan         : " + GolStaff)
print("Status Menikah   : " + Status)
print("Jumlah Anak      : " + str(JmlhAnak))
print("-----------------------------")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Tunjangan Menikah: Rp.", int(TunjMenikah))
print("Tunjangan Anak   : Rp.", int(TunjAnak))
print("|||||||||||||||||||||||||||||||")
print("Gaji Kotor       : Rp.", int(GajiKotor))
print("Potongan (" + str(Persen) + "%)  : Rp.", int(potongan))
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Gaji Bersih      : Rp.", int(GajiBersih))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

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