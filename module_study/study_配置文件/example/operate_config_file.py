import configparser

config = configparser.ConfigParser()

# 1-查看配置文件的section
print(config.sections())

config.read("example.ini", encoding="utf-8")
print(config.sections())

# 添加某一个section
try:
    var = config.add_section("YOLO")
except Exception as e:
    print("该section已经存在 -- %s" % e)
print(config.sections())

# 设置option的值

config.set('YOLO', 'age', '22')
print(config['YOLO']['age'])

config.write(open("example.ini", 'w'))

# 检查
print('DEFAULT' in config)
print('post' in config['topsecret.server.com'])
print(config.has_section('dou'))
print(config.has_option('YOLO', 'height'))

# 2-获取配置文件中的option的值
def get_option_value():
    option_value = config['topsecret.server.com']['port']
    print(option_value)

    topsecret = config['topsecret.server.com']
    print(topsecret['forwardx11'])

    var = config.get('topsecret.server.com', 'port')
    print(var)


print("-" * 60)

# 3-遍历section
for key in config['topsecret.server.com']:
    print(key)

# 4-获取支持的数据类型
def supported_data_type():
    var = config['topsecret.server.com'].getint('port')
    print(type(var))

    var = config['DEFAULT'].getfloat('compressionlevel')
    print(type(var))

    var = config.getboolean('bitbucket.org', 'Compression')
    print(type(var))

print("-" * 60)


# 回退值
def fall_back():
    '''默认值优先于回退值'''
    topsecret = config['topsecret.server.com']
    var = topsecret.get('port', fallback='500')
    print(var)

    var = topsecret.get("monster", fallback="no such option name")
    print(var)


if __name__ == "__main__":
    supported_data_type()
    fall_back()