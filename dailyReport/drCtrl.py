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

    @check_user_login(isJson=True)
    def post(self):
        desc = self.get_argument("desc")
        extra = self.get_argument("extra")
        msg = DailyReportService.submitDailyReport(self.user_id,desc,extra)
        return None,{"msg":msg},0