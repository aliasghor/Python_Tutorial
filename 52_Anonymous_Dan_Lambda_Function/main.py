lambda_kuadrat = lambda angka : angka ** 2
print(f"Lambda kuadrat = {lambda_kuadrat(5)}")

lambda_pengurangan = lambda angka1, angka2 : angka1 - angka2
print(f"Lambda pengurangan = {lambda_pengurangan(5,-6)}")

data_list = ["Gerry","Mogi","Ali"]
data_list.sort()
print(f"List setelah di sort berdasarkan alfabet = {data_list}")

data_list = ["Gerry","Ali Ganteng","Mogi"]
data_list.sort(key=lambda panjang : len(panjang))
print(f"List setelah di sort berdasarkan banyaknya huruf = {data_list}")

list_angka = list(range(1,10 + 1))

angka_filter = list(filter(lambda angka : angka < 5,list_angka))
print(f"Angka kurang dari 5 = {angka_filter}")

angka_genap = list(filter(lambda angka_genap : angka_genap % 2 == 0,list_angka))
print(f"Angka genap = {angka_genap}")

angka_ganjil = list(filter(lambda angka_ganjil : angka_ganjil % 2 == 1,list_angka))
print(f"Angka genap = {angka_ganjil}")

# Anonymous function
def multiply(num1):
    return lambda num2 : num1 * num2

print(f"First anonymous function result = {multiply(5)(2)}")

second_result = multiply(10)
print(f"Second anonymous function result = {second_result(15)}")