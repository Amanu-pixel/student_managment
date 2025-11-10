import os

DATA_FILE = "students.txt"

def load_students():
    students = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                student_id, name, grade = line.strip().split(',')
                students[student_id] = {'name': name, 'grade': grade}
    return students

def save_students(students):
    with open(DATA_FILE, 'w') as file:
        for student_id, info in students.items():
            file.write(f"{student_id},{info['name']},{info['grade']}\n")

def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[student_id] = {'name': name, 'grade': grade}
    print("Student added successfully!")

def search_student(students):
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        info = students[student_id]
        print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")
    else:
        print("Student not found!")

def display_all(students):
    if not students:
        print("No students in the system!")
        return
    print("\nAll Students:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")

def delete_student(students):
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def main():
    students = load_students()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            search_student(students)
        elif choice == '3':
            display_all(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()