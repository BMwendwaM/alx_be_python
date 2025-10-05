class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = _is_checked_out

class Library:
    def __init__(self):      
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for title in self.__books:
            return title

    def return_book(self, title):
        return self.__books.append(title)
    
    def list_available_books(self):
        for i in self.__books:
            print(i)