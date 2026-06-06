"""
Library Management System

Create a menu-driven Library Management System using Python.

Menu:

1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Library Statistics
8. Exit

Requirements:

1. Add Book

   * Enter Book ID
   * Enter Book Title
   * Enter Author Name
   * Store the book details in a nested dictionary.

2. View All Books

   * Display all books with:

     * Book ID
     * Title
     * Author
     * Availability Status

3. Search Book

   * Search a book using Book ID.
   * Display book details if found.
   * Otherwise display "Book not found".

4. Issue Book

   * Enter Book ID.
   * If the book is available, mark it as issued.
   * If already issued, display a suitable message.

5. Return Book

   * Enter Book ID.
   * Mark the book as available again.

6. Delete Book

   * Delete a book using Book ID.

7. Library Statistics

   * Display:

     * Total Books
     * Available Books
     * Issued Books

8. Exit Program

Data Structure Example:

books = {
101: {
"Title": "Python Basics",
"Author": "John",
"Available": True
}
}

Additional Conditions:

* Use a while loop for the menu.
* Use match-case for menu selection.
* Handle invalid menu choices.
* Prevent duplicate Book IDs.
* Show clear messages for every operation.
"""

library = {}
while True:
    print("Welcome to library")
    print("""Menu:

        1. Add Book
        2. View All Books
        3. Search Book
        4. Issue Book
        5. Return Book
        6. Delete Book
        7. Library Statistics
        8. Exit""")
    
    choice = int(input("Enter the choice: "))
    match choice:
        case 1:
            Book_id = int(input("Enter the book id: "))
            Book_title = input("Enter the book title: ")
            Author_name = input("Enter the author name: ")
            Available = input("y for yes and n for no: ")

            library[Book_id]={
            
                "Title": Book_title,
                "Author": Author_name,
                "Avail": Available

            }
            print("Book done")
        case 2:
            if len(library)>0:
                print(library)
            else:
                print("empty")
        case 3:
            id = int(input("Enter the id to seuarch: "))
            if (id in library):
                print("Book found")
                print(library)
            else:
                print("Book not found")
        case 4:
            id = int(input("Enter the id to seuarch: "))
            if(library[Book_id]["Avail"]=="y"):
                print("Book is available " \
                "now issued")
                library[Book_id]["Avail"]="n"
            else:
                print("Issued")
        case 5:
            id = int(input("Enter the id to seuarch: "))
            library[Book_id]["Avail"]="y"
            print("Book returned")
        case 6:
            id = int(input("Enter the id to seuarch: "))
            if id in library:
                print("Deleted")
                del library[Book_id]
            else:
                print("book not present")
        case 7:
            print(f"Total books {len(library)}")
            books_h=0
            books_n=0
            for books in library.values():
                if books["Avail"]=="y":
                    books_h+=1
                else:
                    books_n+=1
            print(f"books ={books_h} books n={books_n}")
        case 8:
            print("👍")

    
        





