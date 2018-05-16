# coding: utf-8

import tornado
from loginService import *
from basic.baseHandler import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render("../templates/login.html")

    def post(self):
        userName = self.get_argument("userName")
        password = self.get_argument("password")
        ck = LoginService.checkPsw(self, userName, password)
        if ck>0:
            self.redirect("/")
        elif ck==-1:
            self.commonError("不存在的用户")
        else:
            self.commonError("用户名或密码错误")