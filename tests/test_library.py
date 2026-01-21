import unittest
from src.library import Library, LibraryError


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    # -------- Sprint 1 tests --------
    def test_add_book_success(self):
        self.lib.add_book(1, "Python", "Guido")
        self.assertIn(1, self.lib.books)

    def test_duplicate_book_raises_error(self):
        self.lib.add_book(1, "Python", "Guido")
        with self.assertRaises(LibraryError):
            self.lib.add_book(1, "Python", "Guido")

    # -------- Sprint 2 tests --------
    def test_borrow_available_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.assertTrue(self.lib.books[1]["borrowed"])

    def test_borrow_unavailable_book_raises_error(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        with self.assertRaises(LibraryError):
            self.lib.borrow_book(1)

    def test_return_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.lib.return_book(1)
        self.assertFalse(self.lib.books[1]["borrowed"])


if __name__ == "__main__":
    unittest.main()
    # -------- Sprint 3 tests --------
    def test_report_contains_header(self):
        report = self.lib.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        self.lib.add_book(1, "Python", "Guido")
        report = self.lib.generate_report()
        self.assertIn("1 | Python | Guido | Available", report)
