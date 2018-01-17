# -*- coding: utf-8 -*-
# 表单验证模块

from wtforms import StringField,IntegerField
from wtforms import Form
from wtforms.validators import InputRequired,Length,Email,EqualTo

class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'),InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20,message='密码长度为6-20位'),InputRequired(message='请输入密码')])
    remember = IntegerField()

class ResetpwdForm(Form):
    oldpwd = StringField(validators=[Length(6, 20, message='密码长度为6-20位'), InputRequired(message='请输入密码')])
    newpwd = StringField(validators=[Length(6, 20, message='密码长度为6-20位'), InputRequired(message='请输入密码')])
    newpwd2 = StringField(validators=[EqualTo(newpwd,message='新密码不一致')])