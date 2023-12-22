data_numbers = [5,5,5,2,3,1,4,5,6,7,8,9,0,10,10,2,3,5,6]
data_names = ["Gerry","Manto","Sampi","Mogi","Balu","Pace"]
print(f"Data numbers: {data_numbers}")
print(f"Data names: {data_names}")
# Using a method count() in a list
print(20 * "=" + " Using a method count() in a list " + 20 * "=")
data_5 = data_numbers.count(5)
print(f"How much 5 is appeared in a list? the answer is = {data_5}")

data_1 = data_numbers.count(1)
print(f"How much 1 is appeared in a list? the answer is = {data_1}")

# Using a method index() in a list
print(20 * "=" + " Using a method index() in a list " + 20 * "=")

data_pace = data_names.index("Pace")
print(f"data_pace is located in index = {data_pace}")

data_manto = data_names.index("Manto")
print(f"data_pace is located in index = {data_manto}")

# Sorting a numbers and a string list
print(20 * "=" + " Sorting a numbers and a string list " + 20 * "=")
data_numbers.sort()
data_names.sort()

print(f"Data numbers after got sorted = {data_numbers}")
print(f"Data names after got sorted = {data_names}")

# Reverseing a numbers and a string list
print(20 * "=" + " Reverseing a numbers and a string list " + 20 * "=")
data_numbers.reverse()
data_names.reverse()

print(f"Data numbers after got reversed = {data_numbers}")
print(f"Data names after got reversed = {data_names}")