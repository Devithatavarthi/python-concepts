#Create a class Book with:
#instance attributes title, author
#a class variable total_books
#a class method from_string(cls, book_str) that creates an object from "title-author" format
#a static method is_valid_title(title) that checks if title has at least 3 characters
#increment total_books for every book created
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1   # increase count

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) > 3


# Create book using normal constructor
if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")

# Create book using class method
b2 = Book.from_string("Django-Andrew")

print(Book.total_books)