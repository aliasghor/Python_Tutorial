tikus = {
    "Mog":"Mogi",
    "Pi":"Sampi",
    "Ger":"Gerry"
}


tikus_copy = tikus.copy()

# Copy dictionary
print(20 * "=" + " Copy dictionary " + 20 * "=")
print(f"Memory address of tikus: {hex(id(tikus))}")
print(f"Memory address of tikus_copy: {hex(id(tikus_copy))}")

tikus['Bal'] = "Balu"
print(tikus)
print(tikus_copy)

# Pop dictionary
print("\n" + 20 * "=" + " Pop dictionary " + 20 * "=")
dictionary_popped = tikus.pop("Pi")

print(f"Data popped = {dictionary_popped}")
print(f"Data tikus after being popped = {tikus}")

# PopItem dictionary
print("\n" + 20 * "=" + " PopItem dictionary " + 20 * "=")

dictionary_popped_item = tikus.popitem()

print(f"Data popped = {dictionary_popped_item}")
print(f"Data tikus after being popped item = {tikus}")

