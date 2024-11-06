import csv
import os


def addStudent(students_list, name, surname, id):
    student = {
        "name": name,
        "surname": surname,
        "id": id
    }
    students_list.append(student)
    print(f"dodano studenta: {name} {surname}, numer studenta: {id}")


def saveToFile(students_list, fileName="students_Database.csv"):
    fieldnames = ["name", "surname", "id"]
    isCreated = os.path.isfile(fileName)

    with open(fileName, mode='a' if isCreated else 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not isCreated:
            writer.writeheader()
        writer.writerows(students_list)
    print(f"Saved students list to: {fileName}")


def importFromFile(fileName="students_Database.csv"):
    students_list = []
    if os.path.isfile(fileName):
        with open(fileName, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for student in reader:
                students_list.append(student)

        x = len(students_list)
        print(f"wczytano {x} studentow z listy")
    else:
        print(f"Plik nie istinieje, baza studentow w pliku csv zosatala utworzona")
    return students_list

def main():
    wantToContinue = True
    fileName = "students_Database.csv"
    students_list = importFromFile(fileName)
    while wantToContinue:
        f = input("Co chcesz zrobic?"
                  "\n1 - dodac studenta"
                  "\n2 - wypisac liste studentow"
                  "\n3 - usunac studenta po ID"
                  "\nreszta - zamknij program\n")
        if f == '1':
            name = input("Podaj imie: ")
            surname = input("Podaj nazwisko: ")
            id = input("podaj id studenta: ")
            addStudent(students_list, name, surname, id)
            saveToFile(students_list, fileName)
        elif f == '2':
            print("Lista studentow:")
            for student in students_list:
                print(student)
        else:
            wantToContinue = False
            print("Dowidzenia!")

if __name__ == "__main__":
    main()







