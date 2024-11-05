import csv
from datetime import datetime

students = []

attendance_data = {}

def load_file(file_path):
    global students
    if file_path.endswith('.csv'):
        with open(file_path, newline='', encoding='utf-8') as csvfile:  #sczyta po kolei kolejne linijki pliku
            reader = csv.reader(csvfile)
            students = [row[0] for row in reader]

    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            students = [line.strip() for line in txtfile]

def save_file(file_path):
    if file_path.endswith('.csv'):
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile: #zapisuje date i imie/nazwisko ucznia z attendance_data
            writer = csv.writer(csvfile)
            for date, present_students in attendance_data.items():
                for student in present_students:
                    writer.writerow([date, student])

    elif file_path.endswith('.txt'):
        with open(file_path, mode='w', encoding='utf-8') as txtfile:
            for date, present_students in attendance_data.items():
                for student in present_students:
                    txtfile.write(f"{date}: {student}\n")

def attendance(date):
    global attendance_data
    if date not in attendance_data:
        attendance_data[date] = []

    print(f"Obecność dnia {date}")
    for student in students:
        status = input(f"Czy {student}jest obecny? (y/n)").strip().lower()
        if status == "y":
            if student in attendance_data:
                attendance_data[date].append(student)
                print("Student został oznaczony jako 'obecny'")
            elif status == "n":
                print("Student został oznaczony jako 'nieobecny'")
                continue
            else:
                print("Niepoprawny input. Student został pominięty i oznaczony jako 'nieobecny'")

    print("Obecność zapisana")
def edit_attendance(date):
    if date in attendance_data:
        print(f"Edytuje obecność dnia {date}")
        for student in students:
            if student in attendance_data[date]:
                print(f"{student} był obecny")
            else:
                print(f"{student} był nieobecny")

            status = input("Czy chcesz zmienić status? (y/n)").strip().lower()
            if status == "y":
                if student in attendance_data:
                    attendance_data[date].remove(student)
                    print("Student został oznaczony jako 'nieobecny'")
                else:
                    attendance_data[date].append(student)
                    print("Student został oznaczony jako 'obecny'")

    print("Obecność zaaktualizowana")



