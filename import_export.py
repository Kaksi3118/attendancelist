import csv

class ImportExportClass:
    def __init__(self):
            self.studentsAttendance = []
    def import_students(self, filename):
            try:
                with open(filename, newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.studentsAttendance = [row for row in reader]

            except Exception as e:
                print(f"Blad podczas importowania: {e}")
            return self.studentsAttendance


    def export_attendance(self, filename):
            try:
                if filename.endswith('.csv'):
                    with open(filename, 'w', newline='', encoding='utf-8') as file:
                        fieldnames = ['Name', 'Present']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(self.students)
             #   elif filename.endswith('.txt'):
              #      with open(filename, 'w', encoding='utf-8') as file:
               #         for student in self.students:
                #            line = f"{student['Name']}: {'Present' if student['Present'] == 'Yes' else 'Absent'}\n"
                 #           file.write(line)
                else:
                    print("Niewlasciwy format pliku. Uzyj .csv lub .txt.")
            except Exception as e:
                print(f"Blad podczas eksportu: {e}")
