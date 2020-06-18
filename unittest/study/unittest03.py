# coding=utf-8
import  unittest


class TestAssert(unittest.TestCase):

    def setUp(self):
        print('\n case before:')
        pass

    def test01(self):
        '''判断相等'''
        a = 1
        b = 1
        self.assertEqual(a, b)
        print('11111')

    def test02(self):
        '''判断a in b'''
        a = 'yolo'
        b = 'yolodoudou'
        self.assertIn(a, b)
        print('22222')

    def test03(self):
        '''判断a is True'''
        a = 3>2
        self.assertTrue(a)
        print('33333')


    def test04(self):
        '''a=b的失败案例'''
        a = 'yolo'
        b = 'doudou'
        self.assertEqual(a, b, msg='失败原因：%s != %s' %(a,b))  # msg参数遇到异常后自定义输出信息
        print('44444')


    def tearDown(self):
        print('\n case end:')
        pass

if __name__ == '__main__':
    unittest.main()
