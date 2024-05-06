"""
    Macam-Macam operator logika bitwise
    - or(|)
    - and(&)
    - xor(^)
    - not(~)
    - shift right(>>)
    - shift left(<<)
"""

# 1. Or(|)
print(20 * "=" + " Operator Bitwise Or(|) " + 20 * "=")

angka1 = 9
angka2 = 5
hasil = angka1 | angka2

print(f"{angka1} memiliki nilai binary = {format(angka1,'08b')}")
print(f"{angka2} memiliki nilai binary = {format(angka2,'08b')}")
print(f"Hasil operator logika bitwise dari {angka1} dan {angka2} adalah = {hasil}")

# 2. And(&)
print(20 * "=" + " Operator Bitwise And(&) " + 20 * "=")

angka1 = 9
angka2 = 5
hasil = angka1 & angka2

print(f"{angka1} memiliki nilai binary = {format(angka1,'08b')}")
print(f"{angka2} memiliki nilai binary = {format(angka2,'08b')}")
print(f"Hasil operator logika bitwise dari {angka1} dan {angka2} adalah = {hasil}")

# 3. Not(~)
print(20 * "=" + " Operator Bitwise Not(~) " + 20 * "=")

angka1 = 0b00001001
hasil = ~angka1

print(f"{angka1} memiliki nilai binary = {format(angka1,'08b')}")
print(f"Hasil operator logika bitwise not dari {angka1} adalah = {hasil}")
print(f"Dan memiliki nilai binary = {format(hasil,'08b')}")
print(f"Nilai binary not dari {hasil} ketika di flip = {format(hasil & 0xFF,'08b')}")

# 4. Shift left
print(20 * "=" + " Shift left(<<) " + 20 * "=")
angka1 = 0b00010001
hasil = angka1 << 1

print(f"{angka1} memiliki nilai binary = {format(angka1,"08b")}")
print(f"{angka1} ketika di shift left = {hasil}")
print(f"Dan variabel hasil memiliki nilai biner = {format(hasil,'08b')}")

# 5. Shift left
print(20 * "=" + " Shift Right(>>) " + 20 * "=")
angka1 = 0b00100101
hasil = angka1 >> 2

print(f"{angka1} memiliki nilai binary = {format(angka1,"08b")}")
print(f"{angka1} ketika di shift right = {hasil}")
print(f"Dan variabel hasil memiliki nilai biner = {format(hasil,'08b')}")