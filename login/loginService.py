# coding: utf-8

import tornado
from utils.db import mydb
import time
import random

class LoginService():

    @staticmethod
    def generateToken():
        p1 = str(time.time().hex())
        p2 = str(int(random.random()*100000.0))
        return p1+p2

    @staticmethod
    def checkPsw(ctrller, user_name, password):
        if not user_name or not password:
            return 0
        res = mydb.get("select id,password from base_user where user_name=%s", user_name)
        if not res:
            return -1
        if res["password"]!=password:
            return 0
        user_id = res["id"]
        token = LoginService.generateToken()
        mydb.execute("update base_user set token=%s where id=%s",token,user_id)
        ctrller.set_cookie('murphyUserId', str(user_id), expires_days=30)
        ctrller.set_cookie('murphyToken', str(token), expires_days=30)
        return user_id