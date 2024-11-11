import csv
import os
class managingListClass:

    def __init__(self):
            self.students = []

    def addStudent(self, name, surname, id, date, attendance):
        student = {
            "name:": name,
            "surname:": surname,
            "id:": id,
            "date:": date,
            "attendance:": attendance

        }
        self.students.append(student)
        print(f"dodano studenta: {name} {surname}, numer studenta: {id}")
    def checkIfCreated(self, filename):
        try:
            if os.path.isfile(filename):
                print(f"plik {filename} istnieje")
            else:
                fieldnames = ["name:", "surname:", "id:", "date:", "attendance:"]
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                print(f"Nie znaleziono bazy uczniów. \nPusty plik {filename} został utworzony.")
        except Exception as e:
            print(f"Błąd podczas tworzenia pliku: {e}")

    def saveToFile(self, filename):
        fieldnames = ["name:", "surname:", "id:", "date:", "attendance:"]
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(self.students)
        print(f"Saved students list to: {filename}")

    def importFromFile(self, fileName):
        if os.path.isfile(fileName):
            with open(fileName, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for student in reader:
                    self.students.append(student)

            x = len(self.students)
            print(f"wczytano {x} studentow z listy")
        else:
            print(f"Plik nie istinieje")
        return self.selfstudents