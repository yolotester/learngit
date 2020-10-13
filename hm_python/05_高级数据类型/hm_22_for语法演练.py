for num in [1,2,3]:
    print(num)

    # 使用break跳出了循环，循环没有完整结束，所以else缩进的代码不会被执行
    if num == 2:
        break

# 循环结束后，else缩进的代码会执行
else:
    print("会执行吗？")

print("循环结束！")