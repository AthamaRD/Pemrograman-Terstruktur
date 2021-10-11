jarakkota = 795
jarakperliter = 12
totalbensin = jarakkota / jarakperliter
print("Total bensin yang diperlukan untuk sampai di Kota C adalah", totalbensin, "liter")

kapasitastangki = 50
kaliminimalPakBudiharusmengisibensin = int(totalbensin // kapasitastangki)
print("Pak Budi mengisi bensin hingga", kaliminimalPakBudiharusmengisibensin, "kali")
