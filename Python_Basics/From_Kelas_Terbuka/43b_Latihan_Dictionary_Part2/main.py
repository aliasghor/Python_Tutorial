import datetime as dt
import os
import string
import random

data_template = {
    "Name":"Unknown",
    "Age":"Unknown",
    "Major":"Unknown",
    "Student-Id":"Unknown",
    "Borned":"Unknown"
}

students_data = {}

while True:
    os.system("cls")
    print(f"{'Welcome to students database program':^50}")
    print(f"{'Please fill your personal data below':^50}")
    print(50 * "-",end='\n\n')

    students = dict.fromkeys(data_template.keys())

    try:
        students['Name'] = input("Please input your students name: ")
        students['Age'] = int(input("Please input your students age: "))
        students['Major'] = input("Please input your major: ")
        students['Student-Id'] = input("Please input your student id: ")

        YEAR = int(input("Please input your borned year (YYYY): "))     
        MONTH = int(input("Please input your borned month (1-12): "))
        DATE = int(input("Please input your borned date (1-31): "))

        students['Borned'] = dt.date(YEAR,MONTH,DATE)

        KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
        students_data.update({KEY:students})

        print(f"{'KEY':^20} {'NAME':^20} {'AGE':^20} {'MAJOR':^20} {'STUDENT_ID':^20} {'BORNED':^20}")
        print(130 * '-')
        for students in students_data:
            KEY = students
            NAME = students_data[KEY]['Name']
            AGE = students_data[KEY]['Age']
            MAJOR = students_data[KEY]['Major']
            STUDENT_ID = students_data[KEY]['Student-Id']
            BORNED = students_data[KEY]['Borned'].strftime("%x")

            print(f"{KEY:^20} {NAME:^20} {AGE:^20} {MAJOR:^20} {STUDENT_ID:^20} {BORNED:^20}")

    except:
        print("An error occured on the program.please try again")

    is_done = input("Do you want to exit from this program? (Y/N): ")

    if is_done == 'y' or is_done == 'Y':
        break

print("Program students database finished")