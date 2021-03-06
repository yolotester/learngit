import hashlib
import time, random, string, json, base64
from Libs.Log_Util import logger
from Config.Config import *
from Crypto.Cipher import AES


ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
              '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
              '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
              '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
              '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
              '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
              '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
               '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
               '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
               '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
               '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
               '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
               '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
               '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
               '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
               '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
               '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
               '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
               '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
               '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
               '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
               '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
               '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
               '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
               '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
               '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
               '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
               '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
               '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
               '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
               '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
               '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
               '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
               '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
               '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
               '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
               '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
               '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
               '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
               '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
               '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
               '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
               '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
               '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
               '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
               '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
               '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
               '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
               '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
               '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
               '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
               '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
               '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
               '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
               '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
               '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
               '乾', '坤']

def get_point_num(num, count):
    """
    获取小数点后面几位
    :param num: 数字
    :param count: 保留的位数
    :return:
    """
    a, b, c = str(num).partition('.')  # 返回三元元祖
    c = c[:count]
    return '.'.join([a, c])  # 使用 . 连接


def gen_mobile_number():
    """
    随机生成手机号码
    :return:
    """
    char_list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char_list2 = ["3", "5", "8"]
    str1 = ''.join(random.sample(char_list2, 1))  # 从char_list2序列中随机取1个元素
    str2 = ''.join(random.sample(char_list1, 9))
    return "1" + str1 + str2

def gen_weixin_union_id():
    """
    生成微信UnionId
    :return:
    """
    char_list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
                                                                                                                 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', '_'
                  ]
    str1 = ''.join(random.sample(char_list1, 21))
    return str1


def md5_encrypt(text):
    """
    md5 加密算法
    :param text: 待加密的字符串
    :return:
    """
    hash_md5 = hashlib.md5(text.encode('utf8'))
    md5_str = hash_md5.hexdigest()

    return md5_str


def aes_encrypt(key, text):
    """
    aes加密算法
    :param key: 加密key
    :param text: 待加密的字符串
    :return:
    """
    pass


def password_md5_encrypt(password, key):
    """
    密码MD5加密
    :param password: 原始密码
    :param key:
    :return:
    """
    return md5_encrypt(md5_encrypt(password) + key)


def key_value_convert_to_json(key_value_str, split_str='&'):
    """
    字符串键值对转json格式
    :param key_value_str: 待转字符串
    :param split_str: 以该字符对字符串切片
    :return:
    """
    str_dict = {}
    result_list = []
    str_list = key_value_str.split(split_str)  # 默认分割所有，返回的是列表

    try:
        for s in str_list:
            tmp_list = s.split('=')
            str_dict.update({tmp_list[0]:tmp_list[1]})

        result_list.append(str_dict)

        # dumps方法把python对象转为json格式。
        return json.dumps(str_dict, sort_keys=True, indent=4, separators=(',', ': '))

    except Exception as err:
        raise err


def json_convert_to_key_value(json_object, split_str='&'):
    """
    json对象转为字符串键值对
    :param json_object: json对象
    :param split_str: 字符串 切片字符
    :return:
    """
    key_value_str = ''
    for key, value in json_object.items():
        key_value_str += key + '=' + str(value) + split_str

    print(key_value_str)
    return key_value_str.rstrip(split_str)


#String模块ascii_letters和digits方法，其中ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9
def _random_name(size=1, chars=string.ascii_letters + string.digits):
    # 获得各个长度的数字和字母组合
    return ''.join(random.choice(chars) for _ in range(size) )


def _first_name(size=2, ln=None, fn=None):
    # 如果从fn字符串里取出来的数据与ln相同，则会重新从fn字符串里取数据
    _lst = []
    for i in range(size):
        _item = _random_name(1, fn)
        if ln:
            while _item in ln:
                _item = _random_name(1, fn)
            _lst.append(_item)
        else:
            _lst.append(_item)
    return ''.join(_lst)


def _last_name(size=1, names=None):
    return _random_name(size, names)


def _full_name(lns, fns):
    # 保证姓名里没有相同字母
    _last = _last_name(1, lns)
    return "{}{}".format(_last, _first_name(random.randint(1, 2), _last, fns))


def gen_new_name():
    """
    随机生成新的用户名称
    :return:
    """
    return _full_name(last_names, first_names)


def gen_new_id_card():
    """
    随机生成新的18位身份证号码
    :return:
    """
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(1, 99),
                                          random.randint(1, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]
        print(i)
        print(y)

    return '%s%s' % (x, LAST[y % 11])


def check_id_card_gender(id_card):
    """
    判断身份证性别, 身份证倒数第二位，奇数男性，偶数女性
    :param id_card: 身份证号
    :return: 1-男 ， 2-女
    """
    gender = id_card[-2]
    if int(id_card) % 2 == 0:
        return 2
    else:
        return 1


def get_id_card_birthday(id_card):
    """
    获取身份证中的生日。身份证号第7位到第15位
    :param id_card: 身份证号
    :return:
    """
    birthday = id_card[6:14]
    birthday = birthday[0:4] + '-' + birthday[4:6] + '-' + birthday[6:8]
    return birthday


def gen_new_bankcard_id(length=16, how_many=1):
    """
    随机生成银行卡号
    :param length: 卡号长度 （默认16位）
    :param how_many: 生成多少个 （默认返回1个）
    :return:
    """
    from random import Random
    import copy

    bank_prefix_list = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']
    ]

    def completed_number(prefix, length_):

        ccnumber = prefix
        while len(ccnumber) < (length_ - 1):
            digit = str(generator.choice(range(0, 10)))
            ccnumber.append(digit)

        sum_ = 0
        pos = 0
        reversed_c_cnumber = []
        reversed_c_cnumber.extend(ccnumber)
        reversed_c_cnumber.reverse()
        while pos < length_ - 1:
            odd = int(reversed_c_cnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum_ += odd
            if pos != (length_ - 2):
                sum_ += int(reversed_c_cnumber[pos + 1])
            pos += 2

        checkdigit = int(((sum_ / 10 + 1) * 10 - sum_) % 10)

        ccnumber.append(str(checkdigit))
        return ''.join(ccnumber)

    def bank_card_number(rnd, prefix_list, length_, how_many_):
        result = []
        while len(result) < how_many_:
            ccnumber = copy.copy(rnd.choice(prefix_list))
            result.append(completed_number(ccnumber, length_))
        return result

    generator = Random()
    generator.seed()

    bank_id_list = bank_card_number(generator, bank_prefix_list, length, how_many)

    return bank_id_list


def get_auth_name_and_id_card(file_name=os.path.join(Config().data_path, 'AuthNameData.txt')):
    """
    从文件AuthNameData.txt读取实名信息
    :param file_name: 实名信息数据文件
    :return: 返回真实姓名 和 身份证号（字典）
    """
    with open(file_name) as file:
        auth_info_dict = {}
        file_content = file.readlines()
        for auth_info in file_content:
            auth_name = auth_info.split('----')[2]
            auth_id_card = auth_info.split('----')[3]
            auth_info_dict.update({auth_name:auth_id_card})

    return auth_info_dict


def delete_auth_datafile(delete_keyword, file_name=os.path.join(Config().data_path, 'AuthNameData.txt')):
    """
    从文件AuthNameData.txt中删除已经被使用过的数据行
    :param delete_keyword: 待 删除的数据行关键字
    :param file_name: 实名信息数据文件
    :return:
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()  # 读取文件中的每一行
    with open(file_name, 'w') as f_w:
        for line in lines:
            if delete_keyword in line:
                continue  # 跳过该层循环，即不把这一行写入文件
            f_w.writelines(line)


if __name__ == '__main__':
    print(password_md5_encrypt('aaaa1111', '9999'))
    print(password_md5_encrypt('aaaa2222', '8888'))
    print(password_md5_encrypt('2222', '8888'))
    str_ = '934b535800b1cba8f96a5d72f72f1611'
    print(md5_encrypt('2222'))
    assert md5_encrypt('2222') == str_, '出错了'

    # print(get_auth_name_and_id_card())
    print(gen_new_id_card())
    print(_full_name(lns='Ak', fns='ASDF'))
    print(_random_name())
    print(json_convert_to_key_value({"1":"12"}))
    print(key_value_convert_to_json('1=12'))

    mobile_number = gen_mobile_number()
    print(mobile_number)
    logger.info(gen_weixin_union_id())
