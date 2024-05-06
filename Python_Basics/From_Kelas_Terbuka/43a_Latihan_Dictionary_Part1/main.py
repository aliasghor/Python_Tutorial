import datetime as dt
import os

data_dict_template = {
    "Name":"Unknown",
    "Age":"Unknown",
    "Student-Id":"Unknown",
    "Borned In":"Unknown"
}

students = dict.fromkeys(data_dict_template.keys())

while True:
    os.system("cls")
    print("Selamat Datang")
    print("Di Program DataBase Mahasiswa")
    print('\n')

    print("Silahkan masukan data pribadi anda")

    students['Name'] = input("Please fill your name: ")
    students['Age'] = int(input("Please fill your age: "))
    students['Student-Id'] = input("Please fill your students-id: ")
    year = int(input("Please fill your borned year(YYYY): "))    
    month = int(input("Please fill your borned month(1-12): "))
    day = int(input("Please fill your borned day(1-31): "))

    students['Borned In'] = dt.date(year,month,day)

    print(students)

    is_quit = input("Do you want to exit this program? (Y/N) ")
    if is_quit == 'Y' or is_quit == 'y':
        os.system("cls")
        break

print("Program finished")


