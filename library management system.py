class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None

class Library:
    def __init__(self):
        self.book = Book("Wings of Fire")
        self.patron = None

    def register_patron(self, name):
        self.patron = Patron(name)
        print(name, "registered successfully.")

    def issue_book(self):
        if self.book.available:
            self.book.available = False
            self.patron.borrowed_book = self.book.title
            print(self.book.title, "issued to", self.patron.name)
        else:
            print("Book is not available.")

    def return_book(self):
        if self.patron.borrowed_book:
            self.book.available = True
            print(self.book.title, "returned by", self.patron.name)
            self.patron.borrowed_book = None
        else:
            print("No book to return.")

    def show_status(self):
        print("Book:", self.book.title)
        print("Available:", self.book.available)

library = Library()

library.register_patron("Shravani")
library.show_status()

library.issue_book()
library.show_status()

library.return_book()
library.show_status()