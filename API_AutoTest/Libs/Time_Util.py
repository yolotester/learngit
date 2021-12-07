import time
import datetime
import calendar


def get_timestamp(time_level=1):
    """
    返回秒级或毫秒级时间戳
    :param time_level: 时间级别 （1：秒级时间戳  2：毫秒级时间戳）
    :return:
    """
    t = time.time()  # 获得时间戳
    if time_level == 1:
        time_stamp = int(t)
    elif time_level == 2:
        time_stamp = int(round(t*1000))  # round（x，n）当n不存在时，返回一个整数，n是小数位
    else:
        raise TypeError('时间戳级别类型错误！')

    return time_stamp

def now_yes_time():
    """
    获取当前时间 和 前一天的时间
    :return:
    """
    now_time = datetime.datetime.now()
    now_time = now_time + datetime.timedelta(seconds=10)  # 10秒钟的延迟
    now_time_format = now_time.strftime('%Y-%m-%d %H:%M:%S')  # 返回可读格式的当地时间
    print(type(now_time_format))  # <class 'str'>

    yes_time = now_time + datetime.timedelta(days=-1)  # 昨天
    yes_time_format = yes_time.strftime('%Y-%m-%d %H:%M:%S')

    return str(now_time_format), str(yes_time_format)

def split_time(daytime):
    """
    分割时间
    :param daytime:时间字符串（格式：'2016-03-30 09:37:25'）
    :return:
    """
    # 字符串的split方法返回的是 字符串列表
    t1 = daytime.split(" ")[0].split("-")
    t2 = daytime.split(" ")[1].split(":")
    year = t1[0]
    month = t1[1]
    day = t1[2]
    hour = t2[0]
    minute = t2[1]
    second = t2[2]

    return [year, month, day, hour, minute, second]

def compare_time(c_time, start_t, end_t):
    """
    判断c_time 是否在某个时间区间中
    :param c_time: 待判断的时间
    :param start_t: 时间区间开始时间
    :param end_t: 时间区间结束时间
    :return:
    """
    s_time = time.mktime(time.strptime(start_t, "%Y-%m-%d %H:%M:%S"))
    e_time = time.mktime(time.strptime(end_t, "%Y-%m-%d %H:%M:%S"))
    log_time = time.mktime(time.strptime(c_time, "%Y-%m-%d %H:%M:%S"))

    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True

    return False

def cal_time(now_time, end_time):
    """
    计算两个日期相差几天
    :param now_time: 当前时间
    :param end_time: 结束时间
    :return:
    """
    date1 = time.strptime(now_time, "%Y-%m-%d %H:%M:%S")  # time.struct_time(tm_year=2016, tm_mon=3, tm_mday=30, tm_hour=9, tm_min=37, tm_sec=25, tm_wday=2, tm_yday=90, tm_isdst=-1)
    date2 = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
    date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])

    print((date2 - date1).days)
    if (date2-date1).days < 0:  # 意思是如果 结束时间 在 开始时间 之前
        return 0
    else:
        return (date2-date1).days + 1  # 结束时间 和 开始时间是同一天，返回1

def cal_time_second(date1, date2, date_flag_1='-', date_flag_2=':'):
    """
    计算两个日期相差多少秒
    :param date1: 日期1
    :param date2: 日期2
    :param date_flag_1: 前半段的符号标记
    :param date_flag_2: 后半段的符号标记
    :return:
    """
    # mktime 把时间元祖转成时间戳
    # strptime 把该格式的'%Y{a}%m{a}%d %H{b}%M{b}%S'.format(a=date_flag_1, b=date_flag_2
    # 时间字符串转成 时间元祖
    date1 = time.mktime(time.strptime(date1, '%Y{a}%m{a}%d %H{b}%M{b}%S'.format(a=date_flag_1, b=date_flag_2)))
    date2 = time.mktime(time.strptime(date2, '%Y{a}%m{a}%d %H{b}%M{b}%S'.format(a=date_flag_1, b=date_flag_2)))

    return int(abs(date2-date1))  # abs求绝对值

def get_current_time():
    """
    获取当前 日期 和 时间
    :return:
    """
    time_format = "%Y-%m-%d %X"  # %X 本地相应的时间表示
    current_time = time.strftime(time_format, time.localtime())

    return current_time


def get_current_date():
    """
    获取当前日期
    :return:
    """
    date_format = "%Y-%m-%d"
    current_date = time.strftime(date_format, time.localtime())

    return current_date


def get_next_month_of_day(current_date):
    """
    计算下个月的当前天
    :param current_date: 当前日期
    :return:
    """
    t1 = current_date.split(" ")[0].split("-")
    year = int(t1[0])
    month = int(t1[1])
    day = int(t1[0])

    if month == 1:
        if calendar.isleap(year):  # 是闰年返回 True,闰年29天，平年28天
            days = 29
        else:
            days = 28
        if day > days:  # 如果当前天>days, 2月份特殊处理
            next_day = days
        else:
            next_day = day

        next_month = 2

        return next_month, next_day

    if month in (3, 5, 7, 8, 10, 12):
        if day == 31:  # 有else的原因是，12月份过后的1月份，天数也是31天
            next_day = 30
        else:
            next_day = day

        if month == 12:  # 月份在12月时，下个月赋值为1，并给出天数.非12个月时，月份正常加1
            next_month = 1
            if day == 31:
                next_day = 31
        else:
            next_month = month + 1

        return next_month, next_day

    if month in (2, 4, 6, 9, 11):
        next_day = day
        next_month = month + 1
        return next_month, next_day


def get_current_month_start_end_time():
    """
    获取当前月的第一天开始时间 和 最后一天结束时间
    :return:
    """
    day_now = time.localtime()  # 时间元祖 time.struct_time(tm_year=2021, tm_mon=2, tm_mday=27, tm_hour=2, tm_min=30, tm_sec=0, tm_wday=5, tm_yday=58, tm_isdst=0)
    day_begin = '%d-%02d-01 00:00:00' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    w_day, month_range = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码
    day_end = '%d-%02d-%02d 23:59:59' % (day_now.tm_year, day_now.tm_mon, month_range)

    return day_begin, day_end


def get_next_week_date(weekday):
    """
    获取下一个周几的时间
    :param weekday: 1 周一......7 周日。calendar.MONDAY 0 ...... calendar.SUNDAY 6。weekday()函数返回的星期几也是0-6
    :return:
    """
    weekday = int(weekday)  # 防止传入参数不是整数
    date_dict = {
        1:calendar.MONDAY,
        2:calendar.TUESDAY,
        3:calendar.WEDNESDAY,
        4:calendar.THURSDAY,
        5:calendar.FRIDAY,
        6:calendar.SATURDAY,
        7:calendar.SUNDAY
    }
    now = datetime.date.today()  # 获得今天的 年月日
    last_day = now + datetime.timedelta(days=1)  # 今天的 后一天
    one_day = datetime.timedelta(days=-1)  # -1 day, 0:00:00
    t = last_day - one_day
    print('今天的后两天：', t)
    print(last_day.weekday())
    print(date_dict[6])

    # weekday()函数返回的是当前日期所在的星期数
    while last_day.weekday() != date_dict[weekday]:  # while一直循环，直到last_day.weekday()返回的星期几和date_dict[weekday]相等
        last_day -= one_day

    return last_day.strftime('%Y-%m-%d')


test = cal_time('2017-03-30 09:37:25', '2017-03-31 9:37:25')
print(test)

print(get_next_week_date(6))
