from datetime import datetime
from enum import unique
from fileinput import filename
from operator import truth, truediv
from tkinter import wantobjects
from traceback import print_tb
import re
from setuptools.package_index import interpret_distro_name

from check_attendance import CheckAttendanceClass
from import_export import ImportExportClass
import csv
from attendance_data import AttendanceDataClass
from managingList import managingListClass

class importingFunctions: #Dla szybkiego dostepu do wszystkich funkcji
    importExport = ImportExportClass()
    attednanceEditor = AttendanceDataClass(student_list = [])
    checkAttendance = CheckAttendanceClass()
    managingList = managingListClass()



use = importingFunctions() # deklaracja funkcji
use.students = []
filename = "students_Database.csv"
use.managingList.checkIfCreated(filename) # sprawdzenie czy istnieje plik
wantToEnd = False

while wantToEnd == False:
    use.students = use.managingList.importFromFile(filename)
    print("\n" * 100)
    decision = input("Zdecyduj co chcesz zrobic: "
                     "\n1 - Pokaż liste studentów"
                     "\n2 - edytuj liste studentów"
                     "\n3 - dodaj obecność"
                     "\n4 - edytuj obecności"
                     "\nreszta - zakończ\n")
    print("\n" * 100)
    if(decision == "1"):
      for student in use.students:
          print(student)
      _ = input("Press any key to continue...")
    elif(decision == "2"):
        wantToStop = False
        while (wantToStop == False):
            addOrDelete = input("chcesz dodac czy usunac studenta? \n1 - dodaj \n2 - usun \nenter - cofnij\n")
            if addOrDelete == "1":
                    name = input("Podaj imie: ")
                    surname = input("Podaj nazwisko: ")

                    isDuplicate = True
                    while (isDuplicate == True):
                        isDuplicate = False
                        idInput = input("Podaj unikalne id: ")  # string: imie,nazwisko,id,data,obecny
                        for student in use.students:
                            dupeStudent = next((student for student in use.students if student["id:"] == idInput),
                                                   None)
                            if dupeStudent:
                                isDuplicate = True
                                print(f"id: {idInput} juz istnieje")
                                break

                    isDateGood = False
                    while isDateGood == False:
                        isDateGood = True
                        date_text = input("Podaj date dolaczenia: (yyyy.mm.dd)")
                        try:
                            date = datetime.strptime(date_text, "%Y.%m.%d").date()
                        except ValueError:
                            isDateGood= False
                            print("Podano bledna wartosc!")

                    use.managingList.addStudent(name,surname,idInput,date)
                    use.managingList.saveToFile(filename)

            elif addOrDelete == "2":
                idToDelete = input("Podaj id do usuniecia: ")
                use.students = use.managingList.deleteStudent("id:",idToDelete, filename)

            else:
                wantToStop = True

    elif (decision == "3"):
        use.checkAttendance.editPresence(filename)
        use.managingList.saveToFile(filename)
    else:
        wantToEnd = True
