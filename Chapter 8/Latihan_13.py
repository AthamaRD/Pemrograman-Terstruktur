def maksimal(r):
    tertinggi = 0
    dictionary = {}
    for x in r:
        uas = x.get('uas')
        mid = x.get('mid')
        nilaitertinggi = (mid + 2*uas)/3
        if(nilaitertinggi>tertinggi):
            tertinggi = nilaitertinggi
            dictionary['nim'] = x.get('nim')
            dictionary['nama'] = x.get('nama')
    print('Mahasiswa dengan nilai tertinggi diraih oleh ', dictionary['nama'] ,'dengan NIM', dictionary['nim'])

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

maksimal(nilaiMhs)