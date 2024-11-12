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



    def updateFile(self, filename):
        imp = managingListClass()
        fieldnames = ["name:", "surname:", "id:", "date:", "attendance:"]
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        print(f"updated student list exported to: {filename}")
        self.students = imp.importFromFile(filename)
        imp.saveToFile(filename)

    def importFromFile(self, fileName):
        if os.path.isfile(fileName):
            tempStudentList = []
            with open(fileName, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for student in reader:
                    tempStudentList.append(student)
                self.students = tempStudentList


            x = len(self.students)
            print(f"wczytano {x} studentow z listy")
        else:
            print(f"Plik nie istinieje")
        return self.students

    def deleteStudent(self,key ,idToDelete, filename):
        updt = managingListClass()
        studentToDelete = next((student for student in self.students if student["id:"] == idToDelete), None)
        if studentToDelete:
            print("lista przed usunieciem:")
            for _ in self.students:
                print(_)
            self.students = [student for student in self.students if student != studentToDelete]
            print(f"usunieto {studentToDelete}")
            print("po usunieciu ")
            for _ in self.students:
                print(_)
        else:
            print(f"nie znaleziono studenta o id: {idToDelete}")
        self.students = updt.updateFile(filename)
        
