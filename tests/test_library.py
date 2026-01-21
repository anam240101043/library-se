import unittest
from src.library import Library, LibraryError


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book(1, "Python", "Guido")
        self.assertIn(1, self.lib.books)

    def test_duplicate_book_raises_error(self):
        self.lib.add_book(1, "Python", "Guido")
        with self.assertRaises(LibraryError):
            self.lib.add_book(1, "Python", "Guido")


if __name__ == "__main__":
    unittest.main()
