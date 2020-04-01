import json

from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.libs.helper import is_isbn_or_keyword
from app.spider.yu_book import YuShuBook
from . import web
from app.froms.book import SearchForm
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_models.book import BookCollection, BookViewModel
from ..view_models.trade import TradeInfo


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
    has_in_gifts = False
    has_in_wishes = False

    yu_book = YuShuBook()
    yu_book.search_by_isbn(isbn)
    book = BookViewModel(yu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True

        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    print('================')
    print(isbn)
    print(has_in_gifts)
    print(has_in_wishes)
    print('================')

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book, gifts=trade_gifts_model, wishes=trade_wishes_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)
