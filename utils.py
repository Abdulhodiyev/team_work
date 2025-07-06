from file_manager import read, append, writerows


def get_next_id(filename: str):
    all_rows = read(filename=filename)
    if all_rows:
        return int(all_rows[-1][0]) + 1
    return 1


def add_book():
    book_name = input("Enter book name: ")
    book_author = input("Enter book author: ")
    book_pages = input("Enter book pages: ")
    book_price = input("ENter book price: ")
    book_id = get_next_id(filename="books")
    append(filename="books", data=[book_id, book_name, book_author, book_pages, book_price])
    print("New book is added")


def show_all_books():
    books = read(filename="books")
    if not books:
        print("No books yet")
        return
    else:
        for book in books:
            print(f"iD: {book[0]}\tName: {book[1]}\tAuthor: {book[2]}\tPages: {book[3]}\tPrice: {book[4]}")


def delete_book():
    book_id = input("Enter book id: ")
    books = read(filename="books")

    is_found = False
    new_book = list()

    for book in books:
        if book[0] == book_id:
            is_found = True
        else:
            new_book.append(book)


    if is_found:
        writerows(filename="books", data=new_book)
        print("Book is deleted")
    else:
        print("Book id not found")
