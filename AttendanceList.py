from datetime import datetime
from enum import unique
from fileinput import filename
from operator import truth, truediv
from tkinter import wantobjects
from traceback import print_tb
import re
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


students = []
studentsAttendance = []
use = importingFunctions() # deklaracja funkcji
filename = "students_Database.csv"
use.managingList.checkIfCreated(filename) # sprawdzenie czy istnieje plik
wantToEnd = False
while wantToEnd == False:
    decision = input("Zdecyduj co chcesz zrobic: "
                     "\n1 - Pokaż liste studentów"
                     "\n2 - edytuj liste studentów"
                     "\n3 - dodaj obecność"
                     "\n4 - edytuj obecności"
                     "\nreszta - zakończ\n")

    if(decision == "1"):
      students = use.managingList.importFromFile(filename)
      for student in students:
          print(student)
      _ = input("Press any key to continue...")
    elif(decision == "2"):
        students = use.managingList.importFromFile(filename)
        wantToStop = False
        while (wantToStop == False):
            wantToStopDecision = input("chcesz dodac kolejngo ucznia? \n1 - tak\n") #JESZCZE USUWANIE
            if wantToStopDecision == "1":
                name = input("Podaj imie: ")
                surname = input("Podaj nazwisko: ")
                isDuplicate = True
                while (isDuplicate == True):
                    isDuplicate = False
                    idInput = input("Podaj unikalne id: ")  # string: imie,nazwisko,id,data,obecny
                    for student in students:
                        if student["id:"] == idInput:
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
                isPresentOrNo = False
                while isPresentOrNo == False:
                    attendance = input("Czy byl obecny? y/n")
                    if attendance == "y":
                        attendance = "Yes"
                        isPresentOrNo = True
                    elif attendance == "n":
                        attendance = "No"
                        isPresentOrNo = True
                    else: print("podano bledna wartosc")
                use.managingList.addStudent(name, surname, idInput, date, attendance)
                use.managingList.saveToFile(filename)
            else:
                wantToStopDecision = True

    elif (decision == "3"):
        use.checkAttendance.editPresence(filename)
    else:
        wantToEnd = True
