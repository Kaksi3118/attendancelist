from import_export import ImportExportClass


class AttendanceDataClass:

    def __init__(self, student_list: list,date=None):
        """
        :param student_list: list of dictionaries with student data
        """
        self.students = []
        self.date_text = ""
        self.attendance_list = []

    def edit_presence(self,filenameDate):
            imp = ImportExportClass()
            self.attendance_list = imp.import_students(filenameDate)
            for student in self.attendance_list:
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



'''
            id_ = student["id"]
            if id_ in self.attendance:
                self.attendance[id_] = present
            else:
                print(f"Student does not exist.")
'''
    def get_date(self):
        return self.date

    def get_export_list(self):
        export_list = []
        for id_, student in self.student_list.items():
            student_copy = student.copy()
            student_copy["presence"] = "Present" if self.attendance[id_] else "Absent"
            export_list.append(student_copy)
        return export_list


