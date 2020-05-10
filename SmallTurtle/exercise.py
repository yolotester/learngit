import random
secret = random.randint(1,10)
print('/////////我不是初学者哦/////////////')
temp = input ('你的幸运数字是哪个：')

while isinstance(temp,int):


        temp = input('请重新输入哦')
        guessNumber = int(temp)
        if guessNumber ==secret:
            print(' 你好棒  猜对了')

        else:
            if  guessNumber>secret:
                print('猜的数字大了哦')
            else:
                print('猜的数字小了哦')
        print('game over')
print('请输入数字！')

