from flask import current_app
from app.libs.httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        # 判断数据是否已经在数据库了 数据库有就返回数据库的数据，没有就存数据库  <==这一步可以增加如下内容
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=10):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = len(data['books'])
        self.books = data['books']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
