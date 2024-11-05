def addStudent(students_list, name, coname, id):
    student = {
        "imie" : name
        "Nazwisko" : coname
        "id" : id
    }
    students_list.append(student)
    print(f"dodano studenta: {name} {coname}, numer studenta: {id}")
def main():
    students_list = [
    addStudent(students_list, "adam","dasd", 1)
