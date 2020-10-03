from library import *

print(""" ***************************************
Welcome to Basic Python Library Demo

Action : 
1. Show Books
2. Book Status
3. Add Book
4. Delete Book
5. Refresh Page

Press 'q' to exit .
****************************************
""")
library = Library()

while True:
    action = input("Please select an action : ")
    if(action =="q"):
        print("The program quits . . .")
        break
    elif(action=="1"):
        library.show_books()
    elif(action=="2"):
        name = input("Enter the name of the book you want to check :")
        print("The book is being questioned . . .")
        time.sleep(2)
        library.book_status(name)
    elif(action=="3"):
        name = input("Enter Books Name :")
        writer = input("Enter Wrtier Name :")
        publisher = input("Enter Publisher Name :")
        kind = input("Enter the Book's Kind Name :")
        page = int(input("Enter the Book's Page Name :"))

        new_book = Book(name,writer,publisher,kind,page)
        print("Adding book . . .")
        time.sleep(2)
        library.add_book(new_book)
        print("Book added !")
    elif(action=="4"):
        book = input("Enter the name of the book you want to delete :")
        decision = input("Are you sure you want to delete this book. ( Y / N ) ")
        if(decision == "Y"):
            print("Book deletion is running . . .")
            time.sleep(2)
            library.delete_book(book)
            print("The book was deleted.")



    elif(action=="5"):
        name = input("Enter the name of the book whose page number you want to refresh : ")
        print("Updating page . . . ")
        time.sleep(2)
        library.refresh_page(name)
        print("Page count has been renewed.")
    else:
        print("Unnecessary operation has been entered. Please enter a value between one and five . ")



