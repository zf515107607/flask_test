from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    # DataRequired,当你在当前表格没有输入而进入到下一个表格时，会提示你输入
    username = StringField('用户名',validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码',validators=[DataRequired(message='请输入密码')])
    remember_me = BooleanField("记住我")
    submit = SubmitField('登录')
