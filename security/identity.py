# coding: utf-8

from utils.db import mydb

def is_token_legal(user_id, token):
    if not user_id or not token:
        return False
    res = mydb.get("select id from base_user where token=%s",token)
    if not res:
        return False
    return str(res["id"])==str(user_id)