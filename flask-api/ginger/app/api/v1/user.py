from app.libs.redprint import RedPrint

api = RedPrint('user')


@api.route('/get', methods=['GET'])
def get_user():
    return 'i am lodge'
