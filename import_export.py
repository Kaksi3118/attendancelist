def importStudents(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        students = [line.strip() for line in file.readlines()] 
    return students


def Export(filename, attendanceList):
    with open(filename, 'w', encoding='utf-8') as file:
        for student in attendanceList:
            file.write(f"{student['Name']}, {student['Presence']}\n")



