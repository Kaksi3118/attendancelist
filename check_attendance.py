import csv
from ctypes import c_char_p
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

    else:
        print("Nieprawidłowy format pliku - nie wczytano danych. Upewnij się że dodałeś rozszerzenie pliku na końcu (.txt lub .cvs)")

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

    else:
        print("Nieprawidłowy format pliku - nie zapisano danych. Upewnij się że dodałeś rozszerzenie pliku na końcu (.txt lub .cvs")

def attendance(date):
    global attendance_data
    if date not in attendance_data:
        attendance_data[date] = []

    print(f"Obecność dnia {date}")
    for student in students:
        status = input(f"Czy {student} jest obecny? (y/n)").strip().lower()
        if status == "y":
            attendance_data[date].append(student)
            print("Student został oznaczony jako 'obecny'")
        elif status == "n":
            print("Student został oznaczony jako 'nieobecny'")
            continue
        else:
            print("Niepoprawny input. Student został pominięty i oznaczony jako 'nieobecny'")

    print("Obecność zapisana")

def edit_attendance(date):
    if date in attendance_data: #jeżeli jest taka data - edytuj tą date
        print(f"Edytuje obecność dnia {date}")
        for student in students:
            if student in attendance_data[date]:
                print(f"{student} był obecny")
            else:
                print(f"{student} był nieobecny")

            status = input("Czy chcesz zmienić status? (y/n)").strip().lower()
            if status == "y":
                if student in attendance_data[date]:
                    attendance_data[date].remove(student)
                    print("Student został oznaczony jako 'nieobecny'")
                else:
                    attendance_data[date].append(student)
                    print("Student został oznaczony jako 'obecny'")
        print("Obecność zaaktualizowana")
    else:
        print("Brak zapisanej obecności na ten dzień")


if __name__ == "__main__":
    file_path = input("Podaj ścieżkę do pliku z listą studentów (.txt lub .csv): ").strip()
    load_file(file_path)

    while True:
        print("1.Obecność")
        print("2.Edytowanie obecności")
        print("3.Zapis obecności do pliku")
        print("4.Wyjdź")
        choice = input("")
        if choice == "1":
            global date
            date_str = input("Podaj datę (YYYY-MM-DD): ").strip()  # podaj date obecności
            date = datetime.strptime(date_str, "%Y-%m-%d").date()  # zamienia datę z formatu string na date
            attendance(date)
        elif choice == "2":
            edit_attendance(date)
        elif choice == "3":
            save_path = input("Zapisz plik pod nazwą(.txt lub .csv): ")
            save_file(save_path)
            print("Obecność zapisana do pliku")
        elif choice == "4":
            break
        else:
            print("Zły wybór, spróbuj ponownie")

