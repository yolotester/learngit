# encoding=gbk
# �����ݶ���ת��Ϊ������  ��Ϊpickling���Ѷ�����ת��Ϊ���ݶ���ΪUnpickling
import pickle
tranSit = ['yolo',5,3.241,['doudou',25]]
pickle_file = open('my_list.pkl','wb')
pickle.dump(tranSit,pickle_file)
pickle_file.close()


pickle_file = open('my_list.pkl','rb')
layOver = pickle.load(pickle_file)
print(layOver)
