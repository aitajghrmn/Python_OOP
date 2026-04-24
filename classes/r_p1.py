class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author

        if type(pages) != int:
            raise TypeError("Pages must be integer")

        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

    def is_long(self):
        if self.pages > 300:
            return "This book is long"
        else:
            return "This book is not long"


def find_biggest_book(books):
    biggest = books[0]

    for book in books:
        if book.pages > biggest.pages:
            biggest = book

    return biggest


try:
    b1 = Book("Book1", "Author1", 120)
    b2 = Book("Book2", "Author2", 450)
    b3 = Book("Book3", "Author3", 280)

    books = [b1, b2, b3]

    for book in books:
        book.describe()
        print(book.is_long())

    biggest = find_biggest_book(books)
    print("Biggest book:", biggest.title)

except Exception as e:
    print(e)
