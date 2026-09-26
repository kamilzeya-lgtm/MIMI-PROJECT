import json
import os

FILE_NAME = "library.json"


# Load books
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save books
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# Add book
def add_book(books):
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    save_books(books)
    print("Book added successfully!")


# Search book
def search_book(books):
    book_id = input("Enter Book ID: ")

    if book_id in books:
        book = books[book_id]

        print("\nBook Found!")
        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
    else:
        print("Book not found.")


# Issue book
def issue_book(books):
    book_id = input("Enter Book ID to issue: ")

    if book_id not in books:
        print("Book not found.")
        return

    if not books[book_id]["available"]:
        print("Book is already issued.")
        return

    books[book_id]["available"] = False
    save_books(books)

    print("Book issued successfully!")


# Return book
def return_book(books):
    book_id = input("Enter Book ID to return: ")

    if book_id not in books:
        print("Book not found.")
        return

    if books[book_id]["available"]:
        print("This book is already available.")
        return

    books[book_id]["available"] = True
    save_books(books)

    print("Book returned successfully!")


# Display available books
def display_available_books(books):
    found = False

    print("\n===== AVAILABLE BOOKS =====")

    for book_id, book in books.items():
        if book["available"]:
            found = True

            print("Book ID:", book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("-" * 30)

    if not found:
        print("No books are currently available.")


# Display all books
def display_all_books(books):
    if not books:
        print("No books found.")
        return

    print("\n===== ALL BOOKS =====")

    for book_id, book in books.items():
        status = "Available" if book["available"] else "Issued"

        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)
        print("-" * 30)


# Main program
def main():

    books = load_books()

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Display All Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            search_book(books)

        elif choice == "3":
            issue_book(books)

        elif choice == "4":
            return_book(books)

        elif choice == "5":
            display_available_books(books)

        elif choice == "6":
            display_all_books(books)

        elif choice == "7":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()