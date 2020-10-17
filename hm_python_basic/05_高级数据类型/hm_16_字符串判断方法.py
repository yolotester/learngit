# 1、判断空白字符 -- 空格 或者\t \n \r
space_str = "  \t\n\r"
print(space_str.isspace())


# 2、判断字符串中是否只包含数字
# 都不能判断小数  num_str = "1.75"
# unicode字符串  num_str = "\u00b2"
# 中文数字       num_str = "一千"
num_str = "一千"
print(num_str)
print(num_str.isdecimal())  # 实际开发中，一般使用这个
print(num_str.isdigit())
print(num_str.isnumeric())
