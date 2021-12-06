try:
    myFile = open("text2biodata.txt","r")
    list = []
    baca = myfile.readlines()

    for i in range(len(baca)):
        split = baca[i].split("|")
        dataDict = {"nim": split[0], "nama": split[1], "alamat": split[2].replace("\n", " ")}
        list += [dataDict]

        print("text2biodata = ", list)
        myfile.close()

except FileNotFoundError:
    print("File yang anda cari tidak ada")
