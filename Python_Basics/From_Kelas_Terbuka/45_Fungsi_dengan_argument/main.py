# Fungsi dengan parameter dan argument

def kali(x,y):
    hasil = x * y
    print(f"{x} x {y} = {hasil}")

kali(5,5)
kali(7,10)

def anggota(list_anggota):
    list_anggota[1] = "Gerry"

    print(f"Data anggota: {list_anggota}")

data = ['gerry','mogi','manto']
anggota(data)