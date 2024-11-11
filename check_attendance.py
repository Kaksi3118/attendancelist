import csv
from ctypes import c_char_p
from datetime import datetime
from managingList import managingListClass



class CheckAttendanceClass:
    def __init__(self):
            self.students = []
            self.attendance_data = {}

    def load_file(self, date):
        self.attendance_data
        fieldnames = ["name:", "surname:", "id:", "date:", "attendance:"]
        with open(file_path, newline='', encoding='utf-8') as csvfile:  #sczyta po kolei kolejne linijki pliku
            reader = csv.reader(csvfile)
            students = [row[0] for row in reader]

    def save_file(self, file_path):

        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile: #zapisuje date i imie/nazwisko ucznia z attendance_data
             writer = csv.writer(csvfile)
             for date, present_students in self.attendance_data.items():
                for student in present_students:
                   writer.writerow([date, student])

    def attendance(self, date):
        self.attendance_data
        if date not in self.attendance_data:
            self.attendance_data[date] = []

        print(f"Obecność dnia {date}")
        for student in self.students:
            status = input(f"Czy {student} jest obecny? (y/n)").strip().lower()
            if status == "y":
                self.attendance_data[date].append(student)
                print("Student został oznaczony jako 'obecny'")
            elif status == "n":
                print("Student został oznaczony jako 'nieobecny'")
                continue
            else:
                print("Niepoprawny input. Student został pominięty i oznaczony jako 'nieobecny'")

        print("Obecność zapisana")

    def edit_attendance(self, date):
        if date in self.attendance_data: #jeżeli jest taka data - edytuj tą date
            print(f"Edytuje obecność dnia {date}")
            for student in self.students:
                if student in self.attendance_data[date]:
                    print(f"{student} był obecny")
                else:
                    print(f"{student} był nieobecny")

                status = input("Czy chcesz zmienić status? (y/n)").strip().lower()
                if status == "y":
                    if student in self.attendance_data[date]:
                        self.attendance_data[date].remove(student)
                        print("Student został oznaczony jako 'nieobecny'")
                    else:
                        self.attendance_data[date].append(student)
                        print("Student został oznaczony jako 'obecny'")
            print("Obecność zaaktualizowana")
        else:
            print("Brak zapisanej obecności na ten dzień")

    def editPresence(self, filename):
        studentList = managingListClass.importFromFile(filename)

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
                self.attendance(date)
            elif choice == "2":
                self.edit_attendance(date)
            elif choice == "3":
                #save_path = input("Zapisz plik pod nazwą(.txt lub .csv): ")
                self.save_file(filename)
                print("Obecność zapisana do pliku")
            elif choice == "4":
                break
            else:
                print("Zły wybór, spróbuj ponownie")


