import configparser
import os


class MyConfig(configparser.ConfigParser):

    def optionxform(self, optionstr):
        return optionstr


class Y_Config(object):

    def __init__(self):

        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_path = os.path.join(self.current_path, 'Config')
        self.v_config_path = os.path.join(self.config_path, 'var_config.ini')

        self.config = MyConfig() # 实例化一个对象
        self.config.read(self.v_config_path, encoding='utf-8')  # 读取var_config.ini

        self.password = self.config.get('Global_Variable', 'UserName')

        self.itmes = self.config.items('Yolo')  # 以列表形式返回Yolo节下的数据[('Age', '18')]

        self.options = self.config.options('Yolo')

        self.sections = self.config.sections()  # ['Global_Variable', 'Yolo', 'Zhao']

        #       has_section
        #       has_option
        #     remove_section(section_name)
        #     remove_option(section_name, option_name)

    def y_get_variable_config(self, variable_name, section_name='Global_Variable'):

        try:
            variable_name = self.config.get(section_name, variable_name)
            return variable_name
        except configparser.NoOptionError as err:
            raise err

    def y_set_variable_config(self, items_name, items_value, section_name):

        self.config.set(section_name, items_name, items_value)
        with open(self.v_config_path, 'w+') as f:
            self.config.write(f)

    def y_add_section(self, section_name='Yolo'):

        self.config.add_section(section_name)

        #  增加配置项
        self.config['Zhao'] = {'Age': '18'}

        with open(self.v_config_path, 'w+') as f:
            self.config.write(f)


if __name__ == '__main__':
    print(Y_Config().current_path)
    print(Y_Config().itmes)
    print(Y_Config().options)
    print(Y_Config().sections[1])  # 返回的是列表中第二个section，因为列表数据下标从0开始

    # Y_Config().y_add_section('Zhao')

    print(Y_Config().y_get_variable_config('Age', 'Yolo'))

