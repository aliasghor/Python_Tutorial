# 1.Membuat segitiga siku-siku menggunakan for loop
sisi = 10
count = 1
print(20 * '=' + '1. Awal dari for loop' + 20 * '=')
for i in range(sisi):
    print("*" * count)
    count += 1
print(20 * '=' + 'Akhir dari for loop' + 20 * '=')

# 2.Membuat segitiga siku-siku menggunakan while loop

print("\n" + 20 * '=' + ' 2.Membuat segitiga siku-siku menggunakan while loop ' + 20 * '=')

count = 1

while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

print(20 * '=' + ' Akhir dariwhile loop ' + 20 * '=')

# 3.Membuat segitiga siku-siku menggunakan while loop dan hanya keluarkan angka ganjil saja

print("\n" + 20 * '=' + ' 3.Membuat segitiga siku-siku menggunakan while loop dan hanya keluarkan angka ganjil saja ' + 20 * '=')

count = 1

while True:
    if count % 2 == 0:
        count += 1

    print("*" * count)
    count += 1

    if count > sisi:
        break

print(20 * '=' + ' Akhir dariwhile loop ' + 20 * '=')

# 4.Membuat segitiga sama kaki

print("\n" + 20 * '=' + ' 4.Membuat segitiga sama kaki ' + 20 * '=')

count = 1
spasi = sisi // 2

while True:
    if count % 2:
        print(" " * spasi,"+" *count)
        spasi -= 1
        count += 1

    else:
        count += 1
        continue

    if count > sisi:
        break

print(20 * '=' + ' Akhir dariwhile loop ' + 20 * '=')