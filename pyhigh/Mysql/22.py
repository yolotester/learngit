from pymysql import *

class JD(object):
    def __init__(self):
        # 创建connect连接
        self.conn = connect(host='localhost', port=3306, user='root', password='Zz114963', database='jing_dong',
                       charset='utf8')
        # 创建游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭游标连接
        self.cursor.close()
        # 关闭conne连接
        self.conn.close()

    def select_value(self):

        sql = 'select name from goods where id =1'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res


if __name__ == '__main__':
    jd = JD()
    print(jd.select_value())