import os

def calculate(num1, choice, num2):
    match choice:
        case '+':
            hasil = num1 + num2

        case '-':
            hasil = num1 - num2

        case '/':
            hasil = num1 / num2

        case '*' | 'x':
            hasil = num1 * num2

        case _:
            print(f"Error unknown choice {choice}")

    return hasil


while True:
    os.system("cls")
    masukan_angka_pertama = int(input("Masukan angka pertama: "))
    pilih_opsi = input("Silahkan pilih opsi antum (+,x,/,-) ")
    masukan_angka_kedua = int(input("Masukan angka kedua: "))

    result = calculate(masukan_angka_pertama, pilih_opsi, masukan_angka_kedua)
    print(f"Your result = {result:,}")

    is_quit = input("Do you want to quit? (Y/N) ")
    os.system("cls")
    if is_quit == 'Y' or is_quit == 'y':
        os.system("cls")
        break

print("Thankyou For trying my simple calculator program")