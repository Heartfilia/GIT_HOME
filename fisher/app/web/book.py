import json

from flask import jsonify, request, flash, render_template

from app.libs.helper import is_isbn_or_keyword
from app.spider.yushu_book import YuShuBook
from . import web
from app.froms.book import SearchForm
from ..view_models.book import BookCollection, BookViewModel


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_keyword(q)
        yu_book = YuShuBook()

        if isbn_or_key == 'word':
            yu_book.search_by_keyword(q, page)
        else:
            yu_book.search_by_isbn(q)

        books.fill(yu_book, q)
    else:
        flash('没有找到需求的信息')
    return render_template('search_result.html', books=books)

# 积分下载判断
# web.route('/download')
# def download():
#    if score > xxx:
#        send_static_file....


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yu_book = YuShuBook()
    yu_book.search_by_isbn(isbn)
    book = BookViewModel(yu_book.first)
    return render_template('book_detail.html', book=book, gifts=[], wishes=[])
