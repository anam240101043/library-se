class LibraryError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {}

    # Sprint 1: Add book
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise LibraryError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }

    # Sprint 2: Borrow book
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise LibraryError("Book not found")
        if self.books[book_id]["borrowed"]:
            raise LibraryError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    # Sprint 2: Return book
    def return_book(self, book_id):
        if book_id not in self.books:
            raise LibraryError("Book not found")
        self.books[book_id]["borrowed"] = False

    # Sprint 3: Generate report
    def generate_report(self):
        report = "Book ID | Title | Author | Status\n"
        report += "-" * 40 + "\n"
        for book_id, info in self.books.items():
            status = "Borrowed" if info["borrowed"] else "Available"
            report += f"{book_id} | {info['title']} | {info['author']} | {status}\n"
        return report
