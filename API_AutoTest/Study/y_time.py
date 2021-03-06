import time
import logging
import calendar
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(lineno)s - %(message)s")

"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""

timestamp = time.time()
print("当前时间戳为 %f" % timestamp)

# 以返回浮点数的方式，从时间戳转换为 时间元祖 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=27, tm_hour=2, tm_min=30, tm_sec=0, tm_wday=5, tm_yday=58, tm_isdst=0)
localtime = time.localtime()
print ("当前时间为:",localtime)

# Sat Feb 27 02:34:31 2021
asctime = time.asctime(localtime)
logging.info("最简单的格式化时间方法：%s" % asctime)

# 2021-02-27 03:00:40 接收时间元组，并返回为时间字符串 	time.strftime(fmt[,tupletime])
strftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
logging.info("格式化时间：%s" % strftime)

# 把fmt格式的时间字符串 解析为时间元组。time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
strptime = time.strptime(strftime, "%Y-%m-%d %H:%M:%S")
logging.info(strptime)

# 接受时间元组 并返回 时间戳 time.mktime(tupletime)
mktime = time.mktime(strptime)
logging.info(mktime)

# 获取某月日历
month = calendar.month(2021, 2)
logging.info(month)

# calendar.monthrange(year,month)
# 返回两个整数。第一个是该月最后一天是星期几，第二个是该月最后一天是多少号。日从0（星期一）到6（星期日）;月从1到12
week_day, month_day = calendar.monthrange(2021, 3)
print(week_day, month_day)  # 0 31

print("555555",calendar.MONDAY)
print(calendar.SUNDAY)