# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication
import smtplib
import datetime
import os
import csv
from dailyReport.drService import DailyReportService


dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
file_path = "/tmp"
shortName = "dailyReport"+dateStr+".csv"
filename = os.path.join(file_path, shortName)
dst_file = file(filename, 'wb')
writer = csv.writer(dst_file)
title_arr = ["日期","姓名","部门","本日工作内容","遇到的问题"]
writer.writerow(title_arr)
dailyRes = DailyReportService.getAllDailyReport(dateStr)
for tmp in dailyRes:
    writer.writerow([dateStr,tmp["user_name"],tmp["depart"],tmp["content"],tmp["extra"]])

dst_file.close()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = '2562227696@qq.com'
password = "znpgltztisjsebhe"
to_addr = '2562227696@qq.com'
smtp_server = "smtp.qq.com"

msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

part = MIMEApplication(open(filename,'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=shortName)
msg.attach(part)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()