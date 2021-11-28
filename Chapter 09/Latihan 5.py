print("============================")
print("NIM  NAMA           MID  UAS")
print("============================")

nilai = [{"nim" : "A01" , "Nama" : "Agustina", "mid" : 50, "uas" : 80},
         {"nim" : "A02" , "Nama" : "Budi", "mid" : 40, "uas" : 90},
         {"nim" : "A03" , "Nama" : "Chicha", "mid" : 100, "uas" : 50},
         {"nim" : "A04" , "Nama" : "Donna", "mid" : 70, "uas" : 100},
         {"nim" : "A05" , "Nama" : "Fatimah", "mid" : 70, "uas" : 80}]

for i in nilai:
    print (i["nim"].ljust(6),
          i["Nama"].ljust(12),
          str(i["mid"]).ljust(5),
          str(i["uas"]))