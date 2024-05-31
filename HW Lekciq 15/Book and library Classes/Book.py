class Book: 
    def __init__ (self, title, author, publisher, year, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn

class Library:
    def __init__ (self, name):
        self.name = name 
        self.books = []

    def add_book(self, book): 
        self.books.append(book)

    def find_books(self, author):
        return [book for book in self.books if book.author == author]
    
    def display_book_info(self, isbn):
        found_book = None 
        for book in self.books:
            if book.isbn == isbn: 
                found_book = book
                break 
        if found_book: 
            print(f'{found_book.title}, {found_book.author}. {found_book.publisher}, {found_book.year}, ISBN: {found_book.isbn}')
        else: 
            print(f'Book not found.')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn: 
                self.books.remove(book)
                print(f'Book with ISBN {isbn} removed from the library!')
                break 
        else:
            print(f"Book not found.")
        
        
library = Library("City Library")
book1 = Book("Book One", "Author A", "Publisher X", 2020, "ISBN12345")
book2 = Book("Book Two", "Author B", "Publisher Y", 2021, "ISBN67890")
book3 = Book("Book Three", "Author A", "Publisher Z", 2021, "ISBN12390")

library.add_book(book1)
library.add_book(book2)

library.display_book_info("ISBN12345")

print([book.title for book in library.find_books("Author A")])

library.remove_book("ISBN12345")
library.display_book_info("ISBN12345")


    
