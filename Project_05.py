product = {}
def add_product():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    
    product[product_id] = {
        'name': product_name,
        'price': product_price,
        'quantity': product_quantity
    }
    print(f"Product {product_name} added successfully.")


def Update_product():
    product_id = input("Enter product ID to update: ")
    if product_id in product:
        product_name = input("Enter new product name: ")
        product_price = float(input("Enter new product price: "))
        product_quantity = int(input("Enter new product quantity: "))
        
        product[product_id] = {
            'name': product_name,
            'price': product_price,
            'quantity': product_quantity
        }
        print(f"Product {product_name} updated successfully.")
    else:
        print("Product ID not found.")


def delete_product():
    product_id = input("Enter product ID to delete: ")
    if product_id in product:
        del product[product_id]
        print(f"Product with ID {product_id} deleted successfully.")
    else:
        print("Product ID not found.")

def search_product():
    product_id = input("Enter product ID to search: ")
    if product_id in product:
        print(f"Product ID: {product_id}")
        print(f"Name: {product[product_id]['name']}")
        print(f"Price: {product[product_id]['price']}")
        print(f"Quantity: {product[product_id]['quantity']}")
    else:
        print("Product ID not found.")


def inventory_report():
    if not product:
        print("No products in inventory.")
    else:
        print("Inventory Report:")
        for product_id, details in product.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {details['name']}")
            print(f"Price: {details['price']}")
            print(f"Quantity: {details['quantity']}")
            print("------------------------")


while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Inventory Report")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        Update_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        search_product()
    elif choice == '5':
        inventory_report()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")