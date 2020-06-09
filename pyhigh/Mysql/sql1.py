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

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''显示所有商品'''

        # 执行sql语句
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_cates(self):
        '''显示商品分类'''

        # 执行sql语句
        sql = 'select cate_name from goods;'
        self.execute_sql(sql)

    def show_brands(self):
        '''显示商品品牌'''

        # 执行sql语句
        sql = 'select brand_name from goods;'
        self.execute_sql(sql)
    #
    # def exit(self):
    #     '''退出系统'''
    #
    #     # 执行sql语句
    #     sql = 'exit()'
    #     self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print('-------京东商城--------')
        print('1、查询所有商品')
        print('2、查询商品分类')
        print('3、查询商品品牌')
        print('4、退出京东商城')
        return  input('请输入相应功能的序号:')


    def run(self):
        while True:

            op = self.print_menu()
            if op == "1":
                # 查询所有商品
                self.show_all_items()
            elif op =="2":
                # 查询商品分类
                self.show_cates()
            elif op == "3":
                # 查询商品品牌
                 self.show_brands()
            elif op =="4":
                break
            else:
                 print('输入有误，请重新输入...')



def main():
    # 创建一个京东商城对象
    jd = JD()
    # 调用run方法
    jd.run()

if __name__ == "__main__":
    main()