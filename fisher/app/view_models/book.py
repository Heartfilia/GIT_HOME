import json


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [cls.__cut_book_data(data)] if data else [],
            'total': 1 if data else 0,
            'keyword': keyword
        }
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [cls.__cut_book_data(book) for book in data['books']],
            'total': len(data['books']) if data else 0,
            'keyword': keyword
        }
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'author': '、'.join(data['author']),
            'pages': data['pages'] or '',
            'summary': data['summary'],
            'image': data['image'] or '',
        }
        return book

    @classmethod
    def __cut_books_data(cls,  data):
        books = []
        for book in data['books']:
            r = {
                'title': book['title'],
                'publisher': book['publisher'],
                'author': '、'.join(book['author']),
                'pages': book['pages'],
                'summary': book['summary'],
                'image': book['image'],
            }
            books.append(r)

        return books


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.isbn = book['isbn']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])

        return ' /'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        self.total = books.total
        self.keyword = keyword

        self.books = [BookViewModel(book) for book in books.books]
