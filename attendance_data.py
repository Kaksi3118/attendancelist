from sys import exception

class Attendance_Data:

    def __init__(self, student_list: list,date=None):
        """
        :param student_list: list of dictionaries with student data
        """
        self.student_list = {student["id"]: student for student in student_list}
        self.attendance = {student["id"]: False for student in student_list}
        self.date = date

    def edit_presence(self, student, present:bool=True):

            id_ = student["id"]
            if id_ in self.attendance:
                self.attendance[id_] = present
            else:
                print(f"Student does not exist.")

    def get_date(self):
        return self.date

    def get_export_list(self):
        export_list = []
        for id_, student in self.student_list.items():
            student_copy = student.copy()
            student_copy["presence"] = "Present" if self.attendance[id_] else "Absent"
            export_list.append(student_copy)
        return export_list


