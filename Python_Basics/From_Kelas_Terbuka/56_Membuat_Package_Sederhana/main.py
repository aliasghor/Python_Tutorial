import package.matematika as mtk
from package.factorial import hitungFactorial as f
from package import binary

# import package.matematika
# from package import matematika
# from package import fisika
# import package.factorial



hasil_kaluklasi_tambah = mtk.calculate(1,2,3,4,5,option='tambah')
print(f"Hasil kalkulasi tambah = {hasil_kaluklasi_tambah}")

hasil_pangkat = mtk.pangkat(5,3)
print(f"Hasil pangkat = {hasil_pangkat}")

hasil_factorial = f(10)
print(f"{hasil_factorial:,}")

hasil_angka_binary = binary.angka_binary

print(f"Angka binary dari {hasil_angka_binary} adalah {format(hasil_angka_binary,'08b')}")