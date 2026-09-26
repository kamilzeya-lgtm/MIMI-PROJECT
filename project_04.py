Employee =[
    {"id": 101, "name": "John Doe", "position": "Manager", "salary": 5000},
    {"id": 102, "name": "Jane Smith", "position": "Developer", "salary": 4000},
    {"id": 103, "name": "Mike Johnson", "position": "Designer", "salary": 3500},
    {"id": 104, "name": "Emily Davis", "position": "Tester", "salary": 3000},
    {"id": 105, "name": "David Wilson", "position": "Support", "salary": 2500}
]
search = input("Enter Employee ID to search: ").lower()
found = False
for employee in Employee:
    if employee["name"].lower()==search or str(employee["id"])==search:
        print(f"Employee ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Position: {employee['position']}")
        print(f"Salary: ${employee['salary']:.2f}")
        found = True
        break