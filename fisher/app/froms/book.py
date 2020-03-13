from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired
#                               长度    数字范围      数据必须有


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='string 1-30')])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='page num 1-99')], default=1)
