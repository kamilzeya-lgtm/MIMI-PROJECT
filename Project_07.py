patients = {}


def add_patient():
    id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")

    patients[id] = {
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor
    }

    print("Patient record added successfully!")


def update_patient():
    pid = input("Enter Patient ID: ")

    if id in patients:
        patients[id]["name"] = input("Enter new name: ")
        patients[id]["age"] = int(input("Enter new age: "))
        patients[id]["disease"] = input("Enter new disease: ")
        patients[id]["doctor"] = input("Enter new doctor name:")

        print("Patient record updated!")
    else:
        print("Patient not found!")


def delete_patient():
    id = input("Enter Patient ID: ")

    if id in patients:
        del patients[id]
        print("Patient record deleted!")
    else:
        print("Patient not found!")


def search_patient():
    id = input("Enter Patient ID: ")

    if id in patients:
        print("\n--- Patient Details ---")
        print("Name:", patients[id]["name"])
        print("Age:", patients[id]["age"])
        print("Disease:", patients[id]["disease"])
        print("Doctor:", patients[id]["doctor"])
    else:
        print("Patient not found!")


def display_patients():
    if not patients:
        print("No patient records available.")
        return

    print("\n===== ALL PATIENT RECORDS =====")

    for id, patient in patients.items():
        print("\nPatient ID:", id)
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Disease:", patient["disease"])
        print("Doctor:", patient["doctor"])


while True:

    print("""
===== HOSPITAL PATIENT RECORD SYSTEM =====

1. Add Patient
2. Update Patient
3. Delete Patient
4. Search Patient
5. Display All Patients
6. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        update_patient()

    elif choice == "3":
        delete_patient()

    elif choice == "4":
        search_patient()

    elif choice == "5":
        display_patients()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")