#  MINI PROJECT - Student Attendance System

students = [("Roni", 201), ("Ebrar", 202), ("Felix", 203), ("Adrian", 204)]

attendance = {
    "Roni": 2,
    "Ebrar": 1,
    "Felix": 3,
    "Adrian": 0
}

present_today = set()

#  Add a new student
def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student = (name, student_id)
    students.append(student)
    attendance[name] = 0
    print("Student added.\n")

# List all registered students
def list_students():
    print("\n All Students:")
    for s in students:
        print(f"Name: {s[0]} | ID: {s[1]}")
    print()

# Mark a student as present today
def mark_attendance():
    name = input("Enter name of student present today: ")
    for s in students:
        if s[0] == name:
            present_today.add(name)
            attendance[name] += 1
            print(f"{name} marked present.\n")
            return
    print("Student not found.\n")

# Show total attendance and today's status
def show_attendance():
    print("\n Attendance Summary:")
    for name in attendance:
        status = "Present Today" if name in present_today else "Absent Today"
        print(f"{name} - Total Days Present: {attendance[name]} | {status}")
    print()

#  Main Menu Loop
while True:
    print("Student Attendance System")
    print("1. Add Student")
    print("2. List Students")
    print("3. Mark Attendance")
    print("4. Show Attendance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        mark_attendance()
    elif choice == "4":
        show_attendance()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.\n")
