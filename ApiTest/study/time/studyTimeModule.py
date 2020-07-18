'''
    目标：掌握time, calendar模块常用方法
'''
import time
import calendar
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(name)s-%(message)s')
logger = logging.getLogger(__name__)

'''
    时间元祖（年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时）
        一周的第几日：0-6
        一年的第几日：0-366
        夏令时：-1,0,1
'''

'''
    python中时间日期格式化符号
    %y  两位数的年份表示（00-99）
    %Y  四位数的年份表示（0000-9999）
    %m  月份（01-12）
    %d  月内的一天（01-31）
    %H  24小时制小时数（0-23）
    %I  12小时制小时数（0-11）
    %M  分钟数（0-59）
    %S  秒（0-59）
    %a  本地简化星期名称
    %A  本地完整星期名称
    %b  本地简化月份名称
    %B  本地完整月份名称
    %%  %本身
    %j  年内的一天（001-366）
    %w  星期（0-6），星期天为星期的开始
    %W  一年中的星期数（0-53）， 星期一为星期的开始
'''
# 获得当前时间戳
# 每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示
# 1593946647.2950757
time.time()
logger.info(time.time())

# 时间戳 --> 时间元祖，默认为当前时间,参数是时间戳
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=5, tm_hour=14, tm_min=58, tm_sec=11, tm_wday=6, tm_yday=187, tm_isdst=0)
time.localtime()
logger.info(time.localtime())
logger.info(time.localtime(1538271871.226226))  # time.struct_time(tm_year=2018, tm_mon=9, tm_mday=30, tm_hour=5, tm_min=44, tm_sec=31, tm_wday=6, tm_yday=273, tm_isdst=0)

# 时间元祖 --> 时间戳
# 1593946691.0
time.mktime((2020, 7, 5, 14, 58, 11, 6, 187, 0))
logger.info(time.mktime((2020, 7, 5, 14, 58, 11, 6, 187, 0)))

# 时间戳 --> 可视化时间
# time.ctime(时间戳) ， 默认为当前时间
# Sun Sep 30 05:44:31 2018   星期 月份 日  时：分：秒  年份
time.ctime()
time.ctime(1538271871.226226)
logger.info(time.ctime(1538271871.226226))

# 时间元祖 --> 可视化时间
# time.asctime(时间元祖)， 默认为当前时间
# Sun Sep 30 05:44:31 2018
time.asctime()
logger.info(time.asctime(time.localtime(1538271871.226226)))

# 时间元祖 --> 可视化时间（定制）
# time.strftime(要转换的格式， 时间元祖)
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
logger.info(time.strftime('%Y-%m-%d-%a %H:%M:%S', time.localtime()))  # 2020-07-05-Sun 15:10:40

# 可视化时间（定制） --> 时间元祖
# time.strptime(时间字符串， 时间格式)
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=5, tm_hour=15, tm_min=10, tm_sec=40, tm_wday=6, tm_yday=187, tm_isdst=-1)
time.strptime('2020-07-05-Sun 15:10:40', '%Y-%m-%d-%a %H:%M:%S')
logger.info(time.strptime('2020-07-05-Sun 15:10:40', '%Y-%m-%d-%a %H:%M:%S'))

# 浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
time.process_time()
logger.info(time.process_time())  # 0.15625


# 获取某年年历
calendar.calendar(2020)
print('以下输出2020年年历：')
print(calendar.calendar(2020))

# 获取某年某月的月历
calendar.month(2020, 7)
print('以下输出2020年7月的月历：')
print(calendar.month(2020, 7))

# 返回在两个年份之间的闰年总数
leapday = calendar.leapdays(2010, 2020)
print(leapday)  # 2

# 相当于print calendar.month(year, month, w=2, l=1)
calendar.prmonth(2020, 7,w=2, l=1)