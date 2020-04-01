from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


#                               长度    数字范围      数据必须有


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='string 1-30')])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='page num 1-99')], default=1)


class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired(),
                                             Length(min=2, max=20, message='收件人姓名长度必须在2到20个字符之间')])
    mobile = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}&', 0, '请输入正确的手机号')])
    message = StringField()
    address = StringField(validators=[DataRequired(), Length(min=10, max=70, message='地址还不到10个字，写详细一点')])
