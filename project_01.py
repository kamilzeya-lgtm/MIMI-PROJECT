import json
import os

FILE_NAME = 'student.json'

def loaded_students():
    if os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def add_student(student):
    students = loaded_students()
    students.append(student)
    with open(FILE_NAME, 'w') as file:
        json.dump(students, file)

def display_students():
    students = loaded_students()
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def search_student(name):
    students = loaded_students()
    for student in students:
        if student['name'] == name:
            return student
    return None

def update_student(name, updated_info):
    students = loaded_students()
    for i, student in enumerate(students):
        if student['name'] == name:
            students[i].update(updated_info)
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
            return True
    return False

def delete_student(name):
    students = loaded_students()
    for i, student in enumerate(students):
        if student['name'] == name:
            del students[i]
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
            return True
    return False

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            add_student({'name': name, 'age': age, 'grade': grade})
            print("Student added successfully.")
        elif choice == '2':
            display_students()
        elif choice == '3':
            name = input("Enter student name to search: ")
            student = search_student(name)
            if student:
                name =input("Enter student name to search: ")
                
                print(f"Found Student - Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            else:
                print("Student not found.")
        elif choice == '4':
            name = input("Enter student name to update: ")
            updated_info = {}
            updated_info['age'] = input("Enter new age (leave blank to keep current): ")
            updated_info['grade'] = input("Enter new grade (leave blank to keep current): ")
            updated_info = {k: v for k, v in updated_info.items() if v}
            if update_student(name, updated_info):
                print("Student updated successfully.")
            else:
                print("Student not found.")
        elif choice == '5':
            name = input("Enter student name to delete: ")
            if delete_student(name):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

main()