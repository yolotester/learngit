'''
    目标：数据库工具类封装
    封装：
        1、主要方法，调用这一个方法就可以操作数据库 def get_sql_one()
        2、辅助方法：封装创建数据库对象
                    封装创建游标对象
                    封装关闭数据库对象
                    封装关闭游标对象
'''
import pymysql

class ReadDB(object):

    # 操作的是同一个数据库对象，则定义为类属性/类方法封装
    conn = None

    # 封装创建数据库对象，先判断数据库对象是否为空,然后返回数据库对象
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect('localhost',
                                       'root',
                                       'Zz114963',
                                       'jing_dong',
                                       charset = 'utf8')

        return self.conn
        print('111')

    # 封装创建游标对象
    def get_cursor(self):
        return self.get_conn().cursor()

    # 封装关闭游标对象,判断游标对象是否为空,为空时关闭游标对象会报异常
    def close_cursor(self, cursor):
        if cursor:  # cursor不为空时
            cursor.close()

    # 封装关闭数据库对象,判断数据库对象是否为空，然后再手动关闭数据库连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #  注意：关闭数据库对象后，对象还存在内存地址中，需要手动关闭
            self.conn = None


    # 主要执行方法
    def get_sql_one(self, sql):

        # 创建游标变量和存放执行sql语句结果的变量data
        cursor = None
        data = None

        # 调用封装好的游标对象,用变量cursor来接受
        cursor = self.get_cursor()

        try:
            # 执行sql 语句
            cursor.execute(sql)

        except Exception as e:
            print('get_sql_one:', e)

        finally:
            # 取出sql语句的结果并赋值给data变量
            data = cursor.fetchone()
            # 关闭游标对象
            self.close_cursor(cursor)

            # 关闭数据库对象
            self.close_conn()

            # 返回数据
            return data

if __name__ == '__main__':
    sql = "select * from goods"
    data = ReadDB().get_sql_one(sql)
    print(data)