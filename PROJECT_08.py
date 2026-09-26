vehicles = []
rentals = []


def add_vehicle():
    vehicle_id = input("Enter Vehicle ID: ")
    name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike): ")
    rent_per_day = float(input("Enter Rent Per Day: "))

    vehicle = {
        "id": vehicle_id,
        "name": name,
        "type": vehicle_type,
        "rent": rent_per_day,
        "available": True
    }

    vehicles.append(vehicle)
    print("Vehicle added successfully!")


def rent_vehicle():
    vehicle_id = input("Enter Vehicle ID to rent: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            if vehicle["available"]:
                customer = input("Enter Customer Name: ")
                days = int(input("Enter Number of Days: "))

                charges = vehicle["rent"] * days

                rental = {
                    "vehicle_id": vehicle_id,
                    "customer": customer,
                    "days": days,
                    "charges": charges
                }

                rentals.append(rental)
                vehicle["available"] = False

                print("Vehicle rented successfully!")
                print("Total Rent:", charges)
                return
            else:
                print("Vehicle is already rented.")
                return

    print("Vehicle not found.")


def return_vehicle():
    vehicle_id = input("Enter Vehicle ID to return: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            if not vehicle["available"]:
                vehicle["available"] = True
                print("Vehicle returned successfully!")
                return
            else:
                print("Vehicle is not rented.")
                return

    print("Vehicle not found.")


def display_vehicles():
    if not vehicles:
        print("No vehicles available.")
        return

    print("\n--- Vehicle List ---")

    for vehicle in vehicles:
        status = "Available" if vehicle["available"] else "Rented"

        print("ID:", vehicle["id"])
        print("Name:", vehicle["name"])
        print("Type:", vehicle["type"])
        print("Rent/Day:", vehicle["rent"])
        print("Status:", status)
        print("-------------------")


def Save_rentals():
    if not rentals:
        print("No rental records.")
        return

    print("\n--- Save Rental Records ---")

    for rental in rentals:
        print("Vehicle ID:", rental["vehicle_id"])
        print("Customer:", rental["customer"])
        print("Days:", rental["days"])
        print("Charges:", rental["charges"])
        print("-------------------")






while True:

    print("\n===== VEHICLE RENTAL MANAGEMENT SYSTEM =====")
    print("1. Add Vehicle")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Display Vehicles")
    print("5. Save Rental Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle()

    elif choice == "2":
        rent_vehicle()

    elif choice == "3":
        return_vehicle()

    elif choice == "4":
        display_vehicles()

    elif choice == "5":
        Save_rentals()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")