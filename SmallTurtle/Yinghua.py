# encoding=gbk
from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()#�±�
    #��ӰЧ��
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#����֦

    if n>0:
        b = random()*15+10 #�ҷ�֧ƫת�Ƕ�
        c = random()*15+10 #���֧ƫת�Ƕ�
        d = l*(random()*0.25+0.7) #��һ����֧�ĳ���
        #��תһ���Ƕ�,���ҷ�֧
        right(b)
        tree(n-1,d)
        #��תһ���Ƕȣ������֧
        left(b+c)
        tree(n-1,d)
        #ת����
        right(c)
    else:
        #��Ҷ��
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)
        #���0.3����Ʈ��Ҷ��
        if(random()>0.7):
            pu()
            #Ʈ��
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #��Ҷ��
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            pu()
            #����
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)#�˻�

bgcolor(0.5,0.5,0.5)#����ɫ
ht()#����turtle
speed(0)#�ٶ� 1-10������0 ���
tracer(0,0)
pu()#̧��
backward(100)
left(90)#��ת90��
pu()#̧��
backward(300)#����300
tree(12,100)#�ݹ�7��
done()
