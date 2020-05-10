# encoding=gbk
# 把数据对象转换为二进制  成为pickling，把二进制转换为数据对象为Unpickling
import pickle
tranSit = ['yolo',5,3.241,['doudou',25]]
pickle_file = open('my_list.pkl','wb')
pickle.dump(tranSit,pickle_file)
pickle_file.close()


pickle_file = open('my_list.pkl','rb')
layOver = pickle.load(pickle_file)
print(layOver)
