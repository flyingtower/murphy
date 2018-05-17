# coding: utf-8

from functools import wraps
from security.identity import *
from constant.const import LOGIN_URL

ERR_MSG = {
    -401: "登录过期,请重新登录",
}

def check_user_login(isJson=False,autoRes=True, redirect=False):
    def _(func):
        @wraps(func)
        def __(ins, *args, **kwargs):
            token = ins.get_cookie('murphyToken')
            user_id = ins.get_cookie('murphyUserId')
            if not is_token_legal(user_id,token):
                ins.redirect(LOGIN_URL)
                return

            ins.set_cookie('murphyToken', token, expires_days=30)
            ins.set_cookie('murphyUserId', user_id, expires_days=30)
            ins.user_id=user_id

            htmlpath, datas, err_code = func(ins, *args, **kwargs)
            if not autoRes:
                return
            if type(datas)=="dict":
                rep = dict()
                if err_code != 0:
                    if not datas.has_key('err_msg'):
                        rep['err_msg'] = ERR_MSG[err_code]
                    if datas:
                        for key, values in datas.iteritems():
                            rep[key] = values
                else:
                    if datas:
                        for key, values in datas.iteritems():
                            rep[key] = values
                rep['err'] = err_code
            else:
                rep = datas
            if isJson:
                ins.write(rep)
            elif redirect:
                ins.redirect(htmlpath)
            elif htmlpath:
                ins.render(htmlpath,data=rep)
        return __
    return _
