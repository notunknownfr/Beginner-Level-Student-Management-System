import pickle
import os


class Student:
    StudentID = 0
    StudentName = ""
    StudentGPA = 0

# THIS FUNCTION ALLOWS YOU TO ADD A RECORD

def add_record():
    id = int(input("Enter Student ID: "))
    print("----------------------------------------------------------")
    name = str.capitalize(input("Enter Student Name: "))
    print("----------------------------------------------------------")
    gpa = float(input("Enter Student GPA: "))
    print("----------------------------------------------------------")
    found = False
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()

    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file:
        TempRecord = pickle.load(file_pointer)
        if id == TempRecord.StudentID:
            found = True
    if found == False:
        if gpa >= 0 and gpa <= 4:
            NewRecord = Student()
            NewRecord.StudentID = id
            NewRecord.StudentName = name
            NewRecord.StudentGPA = gpa
            file_pointer = open("Students.data", "ab")
            pickle.dump(NewRecord, file_pointer)
            file_pointer.close()
            print("Record Added Successfuly!")
        else:
            print("GPA Should Be Between 0.00-4.00!")
    else:
        print("Record With The Given ID Already Exists!")

# THIS FUNCTION PRINTS ALL THE RECORDS

def print_all():
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file:
        TempRecord = pickle.load(file_pointer)
        print("Student ID    : ", TempRecord.StudentID)
        print("Student Name  : ", TempRecord.StudentName)
        print("Student GPA   : ", TempRecord.StudentGPA)
        print("----------------------------------------------------------")
    file_pointer.close()

# THIS FUNCTION ALLOWS YOU TO SEARCH FOR A RECORD BY ID

def search_StuByID():
    SearchID = int(input("Enter The ID Of Student You Want To Search For: "))
    found = False
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file and found == False:
        TempRecord = pickle.load(file_pointer)
        if SearchID == TempRecord.StudentID:
            found = True
            print("----------------------------------------------------------")
            print("Student Name   :", TempRecord.StudentName,"\nStudent GPA    :", TempRecord.StudentGPA)
    if found == False:
        print("----------------------------------------------------------")
        print("Student Not Found!")
    file_pointer.close()

# THIS FUNCTION ALLOWS YOU TO SEARCH FOR A RECORD BY NAME

def search_StuByName():
    SearchName = str.capitalize(input("Enter The Name Of Student You Want To Search For: "))
    print("----------------------------------------------------------")
    found = False
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file and found == False:
        TempRecord = pickle.load(file_pointer)
        if SearchName == TempRecord.StudentName:
            found = True
            print("Student ID   :", TempRecord.StudentID)
            print("Student GPA  :", TempRecord.StudentGPA)
            print("----------------------------------------------------------")
    if found == False:
        print("Student Not Found!")
        print("----------------------------------------------------------")
    file_pointer.close()

# THIS FUNCTION PRINTS THE RECORD OF ALL STUDENTS THAT HAVE GPA HIGHER THAN 3.00

def print_StuGPA():
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file:
        TempRecord = pickle.load(file_pointer)
        if TempRecord.StudentGPA >= 3.0:
            print("Student ID      :", TempRecord.StudentID)
            print("Student Name    :", TempRecord.StudentName)
            print("----------------------------------------------------------")
    file_pointer.close()

# THIS FUNCTION GIVES THE AVERAGE GPA OF ALL THE STUDENTS

def average_GPA():
    count = 0
    sum = 0
    avg = 0
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file:
        TempRecord = pickle.load(file_pointer)
        count = count + 1
        sum = sum + TempRecord.StudentGPA
    avg = sum/count
    print("Average GPA Of Students:", avg)
    file_pointer.close()

# THIS IS A FUNCTION TO DELETE A RECORD

def delete_record():
    DeleteID = int(input("Enter The ID Of Student You Want To Delete: "))
    found = False
    TempRecord = Student()
    file_pointer = open("Students.data", "rb")
    file_pointer2 = open("Temporary.data", "wb")
    file_pointer.read()
    end_of_file = file_pointer.tell()
    file_pointer.seek(0)
    while file_pointer.tell() != end_of_file:
        TempRecord = pickle.load(file_pointer)
        if DeleteID == TempRecord.StudentID:
            found = True
        else:
            pickle.dump(TempRecord, file_pointer2)
    file_pointer.close()
    file_pointer2.close()
    if found == False:
        print("Student Not Found")
        os.remove("Temporary.data")
    else:
        os.remove("Students.data")
        os.rename("Temporary.data", "Students.data")
        print("----------------------------------------------------------")
        print("Record Has Been Removed!")
    file_pointer.close()


# THIS IS THE MAIN MENU OF THE PROGRAM

def menu():
    
    os.system("cls")
    if not os.path.exists("Students.data"):
        open("Students.data", "ab").close()
    choice = 0
    print("--------WELCOME TO THE STUDENT MANAGEMENT DATABASE--------")
    while choice != 8:
        # os.system("cls")
        print("**********************************************************")
        print("(1) Add A Record\n(2) Print All Records\n(3) Search A Student By ID\n(4) Search A Student By Name\n(5) Print The Record Of Students With GPA Higher Than 3.0\n(6) Print The Average Of Student GPA\n(7) Delete A Record\n(8) Exit")
        print("**********************************************************")
        choice = int(input("Enter Your Choice: "))
        print("----------------------------------------------------------")
        if choice == 1:
            add_record()
        elif choice == 2:
            print_all()
        elif choice == 3:
            search_StuByID()
        elif choice == 4:
            search_StuByName()
        elif choice == 5:
            print_StuGPA()
        elif choice == 6:
            average_GPA()
        elif choice == 7:
            delete_record()
menu()