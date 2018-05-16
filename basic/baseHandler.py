# coding: utf-8

import tornado
import json
from tornado.escape import utf8
import datetime
import time

class DateTimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = time.mktime(obj.timetuple())
        else:
            encoded_object = json.JSONEncoder.default(self, obj)
        return encoded_object

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request)
        self.bonduser = None
        self.lang = 'zh-Hans'
        # 判断是否为 post method，提前解析 request body 内容
        if request.method == "POST":
            self.request_method = "POST"
            try:
                self.req = json.loads(self.request.body)
            except:
                self.req = {}
        else:
            self.request_method = "GET"

    def get_argument(self, name, default=[], strip=True):
        if name == 'page':
            arg = super(BaseHandler, self).get_argument(
                name, default or 1, strip)
            return self.check_pages(arg)
        elif name == 'count':
            arg = super(BaseHandler, self).get_argument(
                name, default or 10, strip)
            return self.check_counts(arg)
        arg = super(BaseHandler, self).get_argument(name, default, strip)
        if arg == default and self.request_method == "POST":
            arg = self.req.get(name, default)
        return arg

    def write(self, chunk):
        self._app_err_code = 911
        if self._finished:
            raise RuntimeError("Cannot write() after finish().  May be caused "
                               "by using async operations without the "
                               "@asynchronous decorator.")
        if isinstance(chunk, dict):
            err = chunk.get('err')

            self._app_err_code = err
            chunk = json.dumps(chunk, cls=DateTimeEncoder).replace(
                "</", "<\\/") or json.dumps(chunk).replace("</", "<\\/")
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)

    def commonError(self,errMsg):
        self.render("../templates/error.html",data=errMsg)

    def render(self, template_name, **kwargs):
        # kwargs["static_prefix"] = NEW_STATIC_PREFIX
        # kwargs["is_test"] = IS_TEST
        super(BaseHandler, self).render(template_name, **kwargs)

