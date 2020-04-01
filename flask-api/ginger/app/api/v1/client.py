from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = RedPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
        promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    pass

