from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from ..libs.email import send_mail
from ..models.base import db
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_models.wish import MyWishes


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_wish_counts(isbn_list)
    view_model = MyWishes(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Wish()
            gift.isbn = isbn
            gift.uid = current_user.id

            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')

    return redirect(url_for('book.detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书，请先添加')
    else:
        send_mail(wish.user.email,
                  '有人想送你一本书', 'email/satisfy_wish.html', wish=wish,
                  gift=gift)
        flash('已向TA发送了一封邮件，如果TA愿意接受，你将收到一个鱼漂')
        return redirect(url_for('web.book_detail', isbn=wish.isbn))
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))
