import sqlite3
from termcolor import colored
from tabulate import tabulate
import pandas as pd

# require to install openpyxl to export to excel file


con = sqlite3.connect("books.db")
cur = con.cursor()


def main():
    print("")
    txt1 = "Welcome to the Books Organizer"
    txt2 = "Please choose from below by typing the number \n"
    txt1_center = txt1.center(80)
    txt2_center = txt2.center(80)
    print(colored(txt1_center, "red", attrs=["bold"]))
    print(colored(txt2_center, "blue", attrs=["bold"]))
    welcome_list()


"""
the program first ask the user what s/he want to do
1- ADD book/s, 2- Delete books 3- search book/s 4- export books /Q or q - exit
2- if the user choose add book then ask the user of the numbr of books he want to add
the program ignore non integer postive input and promote again
⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾
"""


def welcome_list():
    print(
        colored(
            "⓵  Add book/s \n⓶  Delete book \n⓷  Search Book \n⓸  Export books \nⓆ  Exit \n",
            "yellow",
        )
    )
    print(colored("YOU CAN PRESS CTRL + C ANY TIME TO EXIT", 'blue', attrs=['bold']))
    while True:
        try:
            user_choice_q = input("Choose number: ")
            if user_choice_q == "Q" or user_choice_q == "q":
                print(colored("Thank you, Goodbye", "red", attrs=["bold"]))
                break
            else:

                user_choice = int(user_choice_q)
                if user_choice == 1:
                    return add_book()
                elif user_choice == 2:
                    return delete_book()
                elif user_choice == 3:
                    return book_search()
                elif user_choice == 4:
                    return library_export_to_excel()
                else:
                    raise ValueError

        except ValueError:
            print("Wrong input please choose from the list")
            pass
        except KeyboardInterrupt:
            print(colored("\nThank you, Goodbye", "red", attrs=["bold"]))
            break


"""
# list of database
id, title*, auther*, category, release_date,
# not all list are reequire, except the title and auther are requird and should promot the user to input again
"""


def add_book():
    while True:
        try:
            num_books_to_add = int(input("How many books you want to add: "))
            if num_books_to_add < 1 or num_books_to_add > 5:
                print(
                    "The",
                    colored("MIN", "red", attrs=["bold"]),
                    "number of books to add is",
                    colored("1", "green", attrs=["bold"]),
                    "and the",
                    colored("MAX", "red", attrs=["bold"]),
                    "for each time is",
                    colored("5", "green", attrs=["bold"]),
                )
            else:
                break
        except ValueError:
            print(
                colored(
                    "Wrong input. Please enter an integer number.",
                    "red",
                    attrs=["bold"],
                )
            )
            pass

    for _ in range(num_books_to_add):
        print("Name of book and auther are required field")
        while True:
            book_name = input("Book name: ").title().strip()
            if not book_name:
                print(
                    "Book name is a requierd filed, please enter the name of the book again!"
                )
            else:
                date_release = input("Release date: ").strip()
                cur.execute(
                    "INSERT INTO books (book, year) VALUES (?, ?)",
                    (
                        book_name,
                        date_release,
                    ),
                )
                book_id = cur.lastrowid
                break

        while True:
            auther_name = input("Auther name: ").title().strip()
            if not auther_name:
                print(
                    "Auther name is a requierd filed, please enter the name of the auther again!"
                )
            else:
                cur.execute(
                    "INSERT INTO writers (book_id, writer) VALUES (?, ?)",
                    (
                        book_id,
                        auther_name,
                    ),
                )
                writer_id = cur.lastrowid
                break

        category_type = str(input("Category: ")).title().strip()
        cur.execute(
            "INSERT INTO categories (book_id, writer_id, category) VALUES (?, ?, ?)",
            (
                book_id,
                writer_id,
                category_type,
            ),
        )

    con.commit()
    print("Book added successfully")
    welcome_list()


def delete_book():
    print(
        colored(
            "Please note: if you delete book it will delete all related information including auther of the book and category",
            "blue",
            "on_magenta",
        )
    )
    print(colored("This can't be undo", "blue", "on_magenta", attrs=["bold"]))
    book_name = input("Book name to delete: ").title().strip()
    cur.execute("SELECT id FROM books WHERE book = ?", (book_name,))
    book_id = cur.fetchone()

    if book_id is None:
        print("Book is not find")
    else:
        cur.execute("DELETE FROM books WHERE id = ?", (book_id[0],))
        cur.execute("DELETE FROM writers WHERE book_id = ?", (book_id[0],))
        cur.execute("DELETE FROM categories WHERE book_id = ?", (book_id[0],))
        con.commit()
        print(colored("Book deleted successfully", 'red', attrs=['bold']))
        print("")

    welcome_list()


def book_search():
    print(
        colored("Search by: \n⓵  Book name \n⓶  Auther name \n⓷  Category  \n", "blue")
    )
    while True:
        try:
            user_choice = int(input("Choose number: "))
            if user_choice == 1:
                book_name = input("Book name: ").title().strip()
                cur.execute("SELECT id FROM books WHERE book = ?", (book_name,))
                book_id = cur.fetchone()

                if book_id is None:
                    print("Book is not find")
                    book_search()
                else:
                    cur.execute(
                        "SELECT books.*, writers.writer, categories.category \
                                FROM books \
                                JOIN writers ON writers.book_id = books.id \
                                JOIN categories ON categories.book_id = books.id \
                                WHERE books.id = ?",
                        (book_id[0],),
                    )
                break

            elif user_choice == 2:
                auther_name = input("Auther name: ").title().strip()
                cur.execute(
                    "SELECT writer FROM writers WHERE writer = ?", (auther_name,)
                )
                auther_name = cur.fetchone()

                if auther_name is None:
                    print("Auther is not find")
                    book_search()
                else:
                    cur.execute(
                        "SELECT books.*, writers.writer, categories.category \
                                FROM books \
                                JOIN writers ON writers.book_id = books.id \
                                JOIN categories ON categories.book_id = books.id \
                                WHERE writers.writer = ?",
                        (auther_name[0],),
                    )
                break

            elif user_choice == 3:
                category = input("Category: ").title().strip()
                cur.execute(
                    "SELECT category FROM categories WHERE category = ?", (category,)
                )
                category = cur.fetchone()

                if category is None:
                    print("Category is not find")
                    book_search()
                else:
                    cur.execute(
                        "SELECT books.*, writers.writer, categories.category \
                                FROM books \
                                JOIN writers ON writers.book_id = books.id \
                                JOIN categories ON categories.book_id = books.id \
                                WHERE categories.category = ?",
                        (category[0],),
                    )
                break

            else:
                raise ValueError

        except ValueError:
            print("Wrong input please choose from the list")
            pass

    rows = cur.fetchall()
    headers = [i[0] for i in cur.description]
    if rows:
        rows.insert(0, headers)  # Add the headers to the beginning of the list
        print(tabulate(rows, tablefmt="grid"))
        print("")
        print(
            colored(
                "Do you want to export the search result to excel?",
                "red",
                attrs=["bold"],
            )
        )
        export_to_excel = input(
            colored(
                "ARE YOU SURE YOU WANT TO CONTINUE(yes/no): ", "blue", attrs=["bold"]
            )
        ).lower()
        if export_to_excel == "yes" or export_to_excel == "y":
            return search_export_excel(rows, user_choice)
        elif export_to_excel == "no" or export_to_excel == "n":
            # print(colored("Thank you, Goodbye", "red", attrs=["bold"]))
            welcome_list()

    return rows, user_choice


def search_export_excel(rows, user_choice):
    headers = [i[0] for i in cur.description]
    df = pd.DataFrame(rows[1:], columns=headers)
    if rows:
        df = pd.DataFrame(rows[1:], columns=headers)
        filename = ""
        if user_choice == 1:
            filename = "search_by_book_name.xlsx"
        elif user_choice == 2:
            filename = "search_by_author_name.xlsx"
        elif user_choice == 3:
            filename = "search_by_category.xlsx"
        df.to_excel(filename, index=False)
        print("Results exported to", filename)
        print("")
    welcome_list()


def library_export_to_excel():
    print(
        colored(
            "This will export all your librare date base to excel file, it may take some times based on your library size",
            "red",
            attrs=["bold"],
        )
    )
    user_choice = input(
        colored("ARE YOU SURE YOU WANT TO CONTINUE(yes/no): ", "blue", attrs=["bold"])
    ).lower()
    if user_choice == "yes" or user_choice == "y":
        try:
            cur.execute(
                "SELECT books.*, writers.writer, categories.category \
                                    FROM books \
                                    JOIN writers ON writers.book_id = books.id \
                                    JOIN categories ON categories.book_id = books.id"
            )
            rows = cur.fetchall()
            headers = [i[0] for i in cur.description]
            if rows:
                df = pd.DataFrame(rows, columns=headers)
                filename = "book_library.xlsx"
            df.to_excel(filename, index=False)
            print("Results exported to", filename)
        except PermissionError:
            print(colored("Please close book_library.xlsx file and try again", "red"))

    elif user_choice == "no" or user_choice == "n":
        print(colored("Thank you, Goodbye", "red", attrs=["bold"]))

    else:
        print(
            colored("Invalid input. Please enter 'yes' or 'no'.", "red", attrs=["bold"])
        )
        return


if __name__ == "__main__":
    main()


"""
ideas for upgrade:
1- program can ask the user of the way he want to export: excel - word - pdf - csv
2*- add shelff ( shelves already exists in book.db)
2- prgram can export one  or more shelf or by auther or realase date ... etc or entire library
 assuming the program (*now 3-9-2023 only export the entire library)
3- fixing max shelf bug
5- add Graphical User Interface
6- add backup
7- adding date of inserting the book in the database
"""
