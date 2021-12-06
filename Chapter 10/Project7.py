file = input('Masukkan nama file : ')
keyword = int(input('Masukkan nilai n : '))
myfile = open (file, 'r')
baca = myfile.read()

list =[]
for i in baca :
    if i.isalpha() :
        shift = ord(i)
        shift -= keyword
        if (shift < ord('A')) :
            shift += 26
        hasil = chr(shift)
    elif i.isspace() :
        hasil = chr(32)
    list += [hasil]

newfile = open('sandi6.txt', 'w')
newfile.write(''.join(list))
myfile.close()
newfile.close()