from operator import attrgetter

from check_attendance import CheckAttendanceClass
from import_export import ImportExportClass
from managingList import managingListClass


class AttendanceDataClass:


    def __init__(self):
        """
        :param student_list: list of dictionaries with student data
        """
        self.students = []
        self.date_text = ""
        self.attendance_list = []

    def editPresence(self,filenameDate):
            imp = managingListClass()
            chck = CheckAttendanceClass()
            #mana = managingListClass()
            self.attendance_list = imp.importFromFile(filenameDate)
            for student in self.attendance_list:
                print(self.attendance_list)
                name = student["name:"]
                surname = student["surname:"]
                attendance = student["attendance:"]
                print(f"Czy chcesz zmienic obecnosc {name} {surname} - ({attendance})? ")
                isPresentOrNo = False
                while isPresentOrNo == False:
                    attendance = input("y/n:")
                    if attendance == "y":
                        attendance = "Yes"
                        isPresentOrNo = True
                    elif attendance == "n":
                        attendance = "No"
                    student["attendance:"] = attendance
            chck.saveAttendance(filenameDate)



    def get_date(self):
        return self.date

    def get_export_list(self):
        export_list = []
        for id_, student in self.student_list.items():
            student_copy = student.copy()
            student_copy["presence"] = "Present" if self.attendance[id_] else "Absent"
            export_list.append(student_copy)
        return export_list


