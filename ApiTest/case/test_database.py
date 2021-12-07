'''
    目标：操作项目数据库，从数据库相关记录断言接口是否成功
'''
# 导包 pymysql
import pymysql

# 创建数据库连接对象
conn = pymysql.connect('localhost',
                       'root',
                       'Zz114963',
                       'jing_dong',
                       charset = 'utf8')

# 创建游标对象，因为方法的返回及执行sql语句后得结果都在游标对象中
cursor = conn.cursor()

# 执行sql语句
sql = 'select * from goods'
cursor.execute(sql)

# 获得sql语句结果并断言,断言时需要从结果取出数据
result = cursor.fetchone()
assert 0 == result[0]

# 关闭游标对象
conn.close()

# 关闭数据库连接对象
cursor.close()