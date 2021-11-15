from random import randint
print("1. Level 1 (Penjumlahan)")
print("2. Level 2 (Pengurangan)")
print("3. Level 3 (Perkalian)")
print("4. EXIT")
level=int(input("Pilih level yang mana?"))
nyawamu=3
skor=0
while True:
    if(nyawamu > 0) and (level==1):
        print("Berapa hasil dari penjumlahan ini guys?")
        x=randint(-100,100)
        y=randint(-100,100)
        z=x+y
        print(x,"+",y)
        jawaban=int(input("hasilnya :"))
        if(jawaban==z):
            skor+=2
        if(jawaban==z):
            print("Hebat banget kamu BENAR, rajin banget. ini skor kamu", skor,"(Heart:", nyawamu,")")
        if(jawaban!=z):
            nyawamu -= 1
            skor -= 2
        if(jawaban!=z):
            print("Yahh jawaban kamu salah ni. Ini skor kamu", skor,"(Heart:", nyawamu,")")
        if(nyawamu==0):
            print("Game Over, better luck next time")
            break
    if (nyawamu > 0) and (level == 2):
        print("Berapa hasil dari penjumlahan ini guys?")
        x = randint(-100, 100)
        y = randint(-100, 100)
        z = x - y
        print(x, "-", y)
        jawaban = int(input("hasilnya :"))
        if (jawaban==z):
            skor += 2
        if (jawaban==z):
            print("Hebat banget kamu BENAR, rajin banget. ini skor kamu", skor, "(Heart:", nyawamu, ")")
        if (jawaban!=z):
            nyawamu-=1
            skor-=2
        if (jawaban!=z):
            print("Yahh jawaban kamu salah ni. Ini skor kamu", skor, "(Heart:", nyawamu, ")")
        if (nyawamu==0):
            print("Game Over, better luck next time")
            break
    if (nyawamu > 0) and (level == 3):
        print("Berapa hasil dari penjumlahan ini guys?")
        x = randint(-100, 100)
        y = randint(-100, 100)
        z = x * y
        print(x, "*", y)
        jawaban = int(input("hasilnya :"))
        if (jawaban == z):
            skor += 2
        if (jawaban == z):
            print("Hebat banget kamu BENAR, rajin banget. ini skor kamu", skor, "(Heart:", nyawamu, ")")
        if (jawaban != z):
            nyawamu -= 1
            skor -= 2
        if (jawaban != z):
            print("Yahh jawaban kamu salah ni. Ini skor kamu", skor, "(Heart:", nyawamu, ")")
        if (nyawamu == 0):
            print("Game Over, better luck next time")
            break
    if (level==4):
        exit()
    if (level != 1) and (level != 2) and (level != 3) and (level != 4):
        print("Levelnya ga tersedia nih bunda, Mohon dibaca dengan Benar")
        break



