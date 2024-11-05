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
