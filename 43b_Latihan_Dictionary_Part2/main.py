import datetime as dt
import os
import random
import string

data_template = {
    "NAME":"UNKOWN",
    "AGE":"UNKOWN",
    "STUDENT-ID":"UNKNOWN",
    "BORNED":"UNKOWN"
}

students_data = {}

while True:
    os.system("cls")
    print("Welcome to student database")
    print("Please fill your personal data",end='\n\n')

    students = dict.fromkeys(data_template.keys())

    students['NAME'] = input("Please input your name: ")
    students['AGE'] = int(input("Please input your age: "))
    students['STUDENT-ID'] = input("Please input your students id: ")
    year = int(input("Please input your borned year (YYYY): "))
    month = int(input("Please input your borned month (1-12): "))
    date = int(input("Please input your borned date (1-31): "))
    students['BORNED'] = dt.date(year,month,date)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    students_data.update({KEY:students})

    print(f"{'KEY':^20} | {'NAME':^20} | {'AGE':^20} | {'STUDENT-ID':^20} | {'BORNED(year,month,date)':^20} | {'BORNED(DAY)'}")

    for student in students_data:
        key = student
        NAME = students_data[key]['NAME']
        AGE = students_data[key]['AGE']
        STUDENT_ID = students_data[key]['STUDENT-ID']
        BORNED = students_data[key]['BORNED'].strftime("%x")
        BORNED_DAY = students_data[key]['BORNED']

        print(f"{key:^20} | {NAME:^20} | {AGE:^20} | {STUDENT_ID:^20} | {BORNED:^20}    | {BORNED_DAY:%A}")

    is_done = input("Do you want to exit from this program? (Y/N): ")
    if is_done == 'y' or is_done == 'Y':
        os.system("cls")
        break

print("Program Finished")