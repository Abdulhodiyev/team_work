from utils import add_book, show_all_books, delete_book

def main():
    print("""
    1. Add book
    2. Show all books
    3. Delete book
    4. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_all_books()
    elif choice == "3":
        delete_book()
    else:
        print("Bye!")
        return

    return main()


if __name__ == "__main__":
    main()