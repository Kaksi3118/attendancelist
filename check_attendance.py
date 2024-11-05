import csv
from datetime import datetime

attendance_data = {}


def load_students_from_file(file_path):
    global students
    if file_path.endswith('.csv'):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            students = [row[0] for row in reader]
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            students = [line.strip() for line in txtfile]
