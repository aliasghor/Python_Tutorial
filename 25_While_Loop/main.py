"""
    contoh operator assignment
    i = 0 <- membuat variabel i dimulai dari 0
    i = i + 1 <- assign ulang nilai variabel i lalu didalam variabel i ane tambahkan dengan i + 1
    jadi logikanya adalah
    
    i = 0
    i = i + 1 <- ini namanya meng assign ulang sebuah nilai.dengan menambahkan nilai 0 + 1 = 1
"""

i = 0 # <- i adalah sebuah "Konvensi" konvensi adalah sebuah penamaan untuk standarisasi looping

while i < 5: # <- Disini ane membikin sebuah kondisi.kondisinya adalah apakah i < 5? Jawabannya True dan akan melakukan looping
    print(f"i sekarang -> {i}") # <- Print i setiap kali berada dalam kondisi True yaitu i < 5
    i += 1 # <- Ini namanya operator assignment kalo gk salah hehe..fungsi operator disini supaya untuk membikin kondisi menjadi False.jadi setiap looping yang terjadi dalam scope ini akan ditambahkan dengan 1

print("Program Selesai")

