import datetime as dt

data_mahasiswa1 = {
    "Nama":"Ali",
    "Umur":20,
    "Beasiswa":False,
    "University":"University Of Wollongong",
    "Tahun Lahir":dt.date(2003,6,6)
}

data_mahasiswa2 = {
    "Nama":"Gerry",
    "Umur":10,
    "Beasiswa":True,
    "University":"ETH Zurich",
    "Tahun Lahir":dt.date(2013,10,11)   
}

data_mahasiswa3 = {
    "Nama":"Mogi",
    "Umur":15,
    "Beasiswa":False,
    "University":"Univeristy Of Oxford",
    "Tahun Lahir":dt.date(2008,12,31)
}

data_mahasiswa = {
    "Mahasiswa1":data_mahasiswa1,
    "Mahasiswa2":data_mahasiswa2,
    "Mahasiswa3":data_mahasiswa3
}

print(f"{'Nama':^15} {'Umur':^15} {'Beasiswa':^15} {'University':^15} {'Tahun Lahir':^20}")
print(80 * "=")

for key in data_mahasiswa:
    KEY = key
    NAMA = data_mahasiswa[KEY]['Nama']
    UMUR = data_mahasiswa[KEY]['Umur']
    BEASISWA = data_mahasiswa[KEY]['Beasiswa']
    UNIVERSITY = data_mahasiswa[KEY]['University']
    TAHUN_LAHIR = data_mahasiswa[KEY]['Tahun Lahir'].strftime("%x")

    print(f"{NAMA:^15} {UMUR:^15} {BEASISWA:^15} {UNIVERSITY:^15} {TAHUN_LAHIR:^20}")