what_number_to_stopped = int(input("Please input a number to stop the iterattion: "))

i = 0

while True:
    print(f"i sekarang -> {i}")
    if i == what_number_to_stopped:
        print(f"Angka berhenti sampe {i}")
        break

    i += 1