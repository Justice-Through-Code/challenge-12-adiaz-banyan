from ast import operator
from operator import attrgetter
from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []
        pass

    def add_title(self, title, author):
        self.books.append(Book(title, author))
        pass

    def count_books(self):
        return len(self.books)

    def remove_title(self, title):
        """Remove a book from the book list"""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
        pass

    def display_books(self):
        # HOW IN THE WORLD DO YOU SORT CASE-INSENSITIVE WITH CLASSES!? I have tried for a while now.
        self.books.sort()
        for book in self.books:
            print(book)
        pass

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []
