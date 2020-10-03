import _sqlite3
import time

class Book():
    def __init__(self,name,writer,publisher,kind,page):
        self.name=name
        self.writer=writer
        self.publisher=publisher
        self.kind=kind
        self.page=page

    def __str__(self):

        return "Book Name: {}\nWriter Name: {}\nPublisher Name: {}\nKind Name: {}\nPage: {}\n".format(self.name,self.writer,self.publisher,self.kind,self.page)

class Library():
    def __init__(self):
        self.connection()

    def connection(self):
        self.connect = _sqlite3.connect("library.db")
        self.cursor = self.connect.cursor()
        query = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, kind TEXT, page INT)"
        self.cursor.execute(query)
        self.connect.commit()

    def disconnection(self):
        self.connect.close()

    def show_books(self):
        query = "Select * From books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        if(len(books) == 0):
            print("No books found in the library !")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def book_status(self,name):
        query = "Select * From books where name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No books found in the library !")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def add_book(self,book):
        query = "Insert into books Values(?,?,?,?,?)"
        self.cursor.execute(query,(book.name,book.writer,book.publisher,book.kind,book.page))
        self.connect.commit()

    def delete_book(self,book):
        query= "Delete From books where name = ? "

        self.cursor.execute(query,(book,))
        self.connect.commit()

    def refresh_page(self,name):
        query = "Select * From books where name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if (len(books)==0):
            print("No books found in the library !")
        else:
            page = books[0][4]
            new_page = int(input("Enter the new page :"))
            page = new_page
            query2 = "Update books set page = ? where name = ?"
            self.cursor.execute(query2,(page,name))
            self.connect.commit()
