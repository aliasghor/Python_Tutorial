def calculate(*args,**kwargs):
    """Sebuah fungsi untuk menghitung tambah dan perkalian"""
    hasil = 0
    if kwargs['option'] == 'tambah':
        for i in args:
            hasil += i

    elif kwargs['option'] == 'kali':
        hasil = 1

        for i in args:
            hasil *= i

    else:
        print(f"Error {kwargs['option']} tidak ditemukan")

    return hasil

pangkat = lambda x, y : x ** y