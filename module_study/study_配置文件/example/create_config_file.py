import configparser

# 实例化对象
config = configparser.ConfigParser()

# 第一种方式：创建了一个section -- [DEFAULT], 三个option = value
config['DEFAULT'] = {'ServerAliveInterval': '45',
                    'Compression': 'yes',
                     'CompressionLevel': '9'}

config['DEFAULT']['ForwardX11'] = 'yes'


# 第二种方式创建 -- config[section][option] = value
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'


# 第三种方式创建
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']  # 个人理解：类对象[section] 赋值给了 字典变量，然后以字典的方式理解
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here


with open('example.ini', 'w') as configfile:
    config.write(configfile)

