class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return 'Книга "{self.name}"'

    def __repr__(self):
        return "Book(id={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books):
        if books is not None:
            self.books = books
        else:
            ...
    def next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1
    def index_by_book_id(self, id):
        for index, book in enumerate(self.books):
            if book.id == id:
                return index
            else:
                raise ValueError("Книги с таким id не существует")
book_1 = Book(id=1, name='One', pages=10)
book_2 = Book(id=2, name='Two', pages=100)
library = Library(books=[book_1, book_2])
print(library.next_book_id())
print(library.index_by_book_id(1))