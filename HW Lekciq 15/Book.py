class Book: 
    def __init__ (self, title, author, pages):
        self. title = title
        self.author = author 
        self. pages = pages 


    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"



book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 192)
print(book1.get_book_info())