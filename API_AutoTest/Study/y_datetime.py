
# from datetime import datetime, date  # datetime模块中有datetime类 和 date类
# https://www.cnblogs.com/baxianhua/p/9928163.html
# import sys
# sys.path.extend(["/Users/zz/Git/API_AutoTest"])
# print(sys.path)


import datetime
import time
from Libs.Log_Util import logger
from datetime import timedelta

# 获取当前日期和时间 2021-02-27 23:10:08.506635
now = datetime.datetime.now()
print(now)

# 获取当前日期 2021-02-28
today = datetime.date.today()
last_day = today + datetime.timedelta(days=1)  # 2021-03-01
one_day = datetime.timedelta(days=-1)  # -1 day, 0:00:00
print(today)
print("111111", last_day)
print("222222", one_day)

# 代表日期的Date对象 2021-02-28
d = datetime.date(2021, 2, 28)
logger.info(d)

# 从时间戳获取日期 2021-02-28
timestamp = datetime.date.fromtimestamp(time.time())
logger.info(timestamp)

# 获取今天的年 月 日
get_data = datetime.date.today()
logger.info("current year: %d", get_data.year)
logger.info("current month: %d", get_data.month)
logger.info("current day: %d", get_data.day)

# 代表时间的time对象 23:52:12.000120
time = datetime.time(hour=23, minute=52, second=12, microsecond=120)
logger.info(time)

# 代表日期时间的datetime对象 可以获得年月日 时分秒 微秒 时间戳
datetime = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
logger.info(datetime.year)
logger.info(datetime)
logger.info(datetime.timestamp())  # 1511884559.34238

# timedelta对象代表 两个日期 或者 时间之间 的差
timedelta = timedelta(seconds=10)
print("121212",timedelta)

now_time = now + timedelta
print(now_time)




