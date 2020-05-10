'''
f = open('D:\\test2',encoding='utf-8',errors='ignore')
boy = []
girl = []
count = 1
# 分割操作
for each_line in f:
    if each_line[:6] != '======':
        (role,spoken) = each_line.split('：',1)
        if role == '女':
            girl.append(spoken)
        if role == '男':
            boy.append(spoken)

#   保存操作
    else:
        file_name_boy = 'Boy_' + str(count) +'.txt'
        file_name_girl = 'Girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count +=1

file_name_boy = 'Boy_' + str(count) +'.txt'
file_name_girl = 'Girl_' + str(count) + '.txt'

boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()
'''

# 优化第二种
def save_file(boy,girl,count):
    file_name_boy = 'Boy_' + str(count) + '.txt'
    file_name_girl = 'Girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    f = open('D:\\test2', encoding='utf-8', errors='ignore')
    boy = []
    girl = []
    count = 1
    # 分割操作
    for each_line in f:
        if each_line[:6] != '======':
            (role, spoken) = each_line.split('：', 1)
            if role == '女':
                girl.append(spoken)
            if role == '男':
                boy.append(spoken)

        #   保存操作
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1

    save_file(boy,girl,count)
    f.close()
split_file('test2.txt')

