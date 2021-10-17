from random import randint
Angka = randint(0, 100)
print ('Hello.. My Name is Mr. Lappie , nah aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100. Kuy ditebak jawabannya?!?!?!')
while True:
    menebak = int(input('Tebakanmu ni : '))
    if menebak > Angka :
        print ('WahWah bilanganmu kegedean tuhh')
    elif menebak < Angka :
        print ('Duh bilanganmu kekecilan ya')
    elif menebak == Angka :
        print ('Mantapp banget tebakanmu BENAR, CONGRATSSS')
        break