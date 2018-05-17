# coding: utf-8

from utils.db import mydb
import datetime
import os
import csv

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
        if not content:
            return "提交失败: 日报不能为空",False
        try:
            todayStr = datetime.datetime.now().strftime("%Y-%m-%d")
            mydb.execute(
                "INSERT INTO daily_report(daily_date,user_id,content,extra) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE content=%s,extra=%s",
                todayStr, user_id, content, extra, content, extra)
        except Exception as e:
            return "提交失败:" + str(e.message),False
        return "提交"+todayStr+"的日报成功",True

    @staticmethod
    def generateGroupDailyReport():
        dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
        file_path = "/tmp"
        shortName = "dailyReport" + dateStr + ".csv"
        filename = os.path.join(file_path, shortName)
        dst_file = file(filename, 'wb')
        writer = csv.writer(dst_file)
        title_arr = ["日期", "姓名", "部门", "本日工作内容", "遇到的问题"]
        writer.writerow(title_arr)
        dailyRes = DailyReportService.getAllDailyReport(dateStr)
        for tmp in dailyRes:
            writer.writerow(
                [dateStr, tmp["user_name"].encode("utf8"), tmp["depart"].encode("utf8"), tmp["content"].encode("utf8"),
                 tmp["extra"].encode("utf8")])
        dst_file.close()
        return filename
