from . import web
from ..models.gift import Gift
from ..view_models.book import BookViewModel


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]


@web.route('/personal')
def personal_center():
    pass
