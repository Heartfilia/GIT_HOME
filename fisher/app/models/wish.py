from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, func, desc
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return gifts

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(
            Gift.isbn).all()
        count_dict_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_dict_list

    @property
    def book(self):
        yu_book = YuShuBook()
        yu_book.search_by_isbn(self.isbn)
        return yu_book.first
