'''
fr = open('d:\\test2.txt',encoding='utf-8')
fr_new = open('d:\\test3.txt','w',encoding='utf-8')
for line in fr:
    if '\r' in line:
        line = line.replace('\r', ' ')
        # 用空格替代回车键
    if '\n' in line:
        line = line.replace('\n', ' ')
    fr_new.write(line)
fr.close()
fr_new.close()
'''
fr_new = open('d:\\test2.txt',encoding='utf-8')
man = []
women = []
count = 1
print(fr_new.read())
for eachline in fr_new:
    print('test2222')

    if eachline[:6] != '===========':
        (role, spoken) = eachline.split('：')
        print('test')
        if role == '女':
            women.append(spoken)
        if role == '男':
            man.append(spoken)

    else:
        file_name_man = 'man_' + str(count) + 'txt'
        file_name_women = 'women_' + str(count) + 'txt'

        man_file = open('file_name_man','w')
        women_file = open('file_name_women', 'w')

        man_file.writelines(man)
        women_file.writelines(women)

        man_file.close()
        women_file.close()

        man = []
        women = []
        count +=1


file_name_man = 'man_' + str(count) + 'txt'
file_name_women = 'women_' + str(count) + 'txt'

man_file = open('file_name_man', 'w')
women_file = open('file_name_women', 'w')

man_file.writelines(man)
women_file.writelines(women)

man_file.close()
women_file.close()


fr_new.close()








