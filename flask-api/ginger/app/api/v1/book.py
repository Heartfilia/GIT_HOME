from app.libs.redprint import RedPrint

api = RedPrint('book')


@api.route('/get', methods=['GET'])
def get_book():
    return 'get book'
