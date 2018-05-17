# coding: utf-8

import tornado.ioloop
import tornado.web
from dailyReport.drCtrl import *
from login.loginCtrl import *
from constant.const import *
import os

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", DailyReportHandler),
            (r"/dr/input/view", DailyReportInputHandler),
            (r"/dr/input/submit", DailyReportInputHandler),
            (r"/dr/download", DailyReportDownloadHandler),
            (LOGIN_URL, LoginHandler),
            ("/login/dologin", LoginHandler),
        ]
        settings = dict(
            gzip=True,
            debug=False,
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'templates/static'),
            cookie_secret='603915d0/1c04=46fa-a0b6+fb49a24b13f2',
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    http_server = Application()
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



