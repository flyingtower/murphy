# coding: utf-8

import tornado
from basic.baseHandler import BaseHandler
from drService import *
from utils.decorator import check_user_login

class DailyReportHandler(BaseHandler):
    @check_user_login(isJson=False)
    def get(self):
        dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
        data = DailyReportService.getAllDailyReport(dateStr)
        return "../templates/dailyReportList.html",{"feeds":data,"dateStr":dateStr},0

class DailyReportInputHandler(BaseHandler):
    @check_user_login(isJson=False)
    def get(self):
        return "../templates/dailyReportInput.html",None,0

    @check_user_login(isJson=False, redirect=True)
    def post(self):
        desc = self.get_argument("desc")
        extra = self.get_argument("extra")
        msg,success = DailyReportService.submitDailyReport(self.user_id,desc,extra)
        if success:
            return "/",None,None
        self.commonError(msg)

class DailyReportDownloadHandler(BaseHandler):
    @check_user_login(isJson=True)
    def get(self):
        filename = DailyReportService.generateGroupDailyReport()
        if filename and len(filename) > 0:
            self.set_header('Content-Type', 'application/force-download')
            self.set_header('Content-Disposition', 'attachment; filename=' + filename)
            buf_size = 4096
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(buf_size)
                    if not data:
                        break
                    self.write(data)
        self.finish()
        return None,None,0


