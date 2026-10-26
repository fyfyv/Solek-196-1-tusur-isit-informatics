class Book:
    def __init__ (self, title, author, isbn, year, pages):
        if pages <= 0: raise ValueError("страниц должно быть больше нуля")
        self._title = title
        self._author =  author
        self._isbn = isbn
        self._year = year
        self._pages = pages
        self._is_available = True
        self._last_read_pages = 0

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if self._is_available :
            self._is_available = False
        else: raise ValueError("книга уже выдана")

    def give_back(self, pages_read):
        if pages_read >= 0:
            if not self._is_available and pages_read <=self._pages:
                self._is_available = True
                self._last_read_pages = pages_read
            else: raise ValueError("значение не валидно")
        else: raise ValueError("значение не может быть отрицательным")

    def __eq__ (self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return (f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})")

class Reader:
    def __init__(self,name):
        self._name = name
        self.books = []
        self.pages_read = 0

class Library:
    def __init__ (self):
        self._books = {}

    def add_book(self,book):
        self._books[book.isbn] = book

    def find_by_isbn(self,isbn):
        return self._books.get(isbn)
        # другой варик
        # if isbn in self._books:
        #     return self._books[isbn]
        # else: return None
    def find_by_author(self, author):
        return [ book for book in self._books.values() if book.author == author]

    def lend(self,isbn, reader):
        if self._books[isbn].is_available:
            self._books[isbn].borrow()
            reader.books.append(self._books[isbn])
        else:
            raise ValueError("книга уже выдана")

    def __len__ (self):
        return len(self._books)

    def available(self):
        return [book for book in self._books.values() if book.is_available]

    def unfinished(self):
        return [book for book in self._books.values() if book.last_read_pages > 0 and book.last_read_pages < book.pages]

    def take_back(self, isbn, reader, pages_read):
        if not self._books[isbn].is_available and self._books[isbn] in reader.books:
            self._books[isbn].give_back(pages_read)
            reader.books.remove(self._books[isbn])
            reader.pages_read += pages_read
        else:
            raise ValueError("книга уже в библиотеке")
