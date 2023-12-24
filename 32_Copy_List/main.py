data_list = ["Gerry","Mogi","Pace","Sampi","Manto"]
data_reference = data_list

if data_list is data_reference:
    print(f"Betul data {data_list} dan data {data_reference} berada didalam 1 memory address atau 1 identity")
    print(f"Memoi address data_lists: {hex(id(data_list))} memory addres data_reference: {hex(id(data_reference))}")

else:
    print(f"Tidak data {data_list} dan data {data_reference} berada pada identity atau memory address yang berbeda")

data_list[0] = "Manto"
print(f"Data lists = {data_list}")
print(f"Data reference = {data_reference}")

data_copy = data_list.copy()

if data_list is data_copy:
    print("Yak data_list dan data_copy berada didalam 1 identity atau memory address")
else:
    print("Tidak data_list dan copy tidak didalam 1 identity atau memory addresss")
