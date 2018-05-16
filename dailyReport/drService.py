# coding: utf-8

from utils.db import mydb
import datetime


class DailyReportService():

    @staticmethod
    def getAllDailyReport(dateStr=None):
        if not dateStr:
            dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
        res = mydb.query("select a.user_name,a.depart,b.content,b.extra from base_user a,daily_report b where a.id=b.user_id and b.daily_date=%s",dateStr)
        if not res:
            return []
        return res

    @staticmethod
    def submitDailyReport(user_id, content, extra):
        try:
            todayStr = datetime.datetime.now().strftime("%Y-%m-%d")
            mydb.execute(
                "INSERT INTO daily_report(daily_date,user_id,content,extra) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE content=%s,extra=%s",
                todayStr, user_id, content, extra, content, extra)
        except Exception as e:
            return "提交失败:" + str(e.message)
        return "提交"+todayStr+"的日报成功"