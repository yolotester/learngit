def testmeasure():


    print("测量开始。。。")
    temp = 39
    wetness = 50
    print("测量结束。。。")

    # 可以使用  元祖   让函数一次返回多个值
    # 如果函数返回的类型是元组， 小括号可以省略
    # return(temp, wetness)
    return temp, wetness

# result存储的是元组类型
result = testmeasure()
print(result)

# 如果函数返回的类型是元组， 同时希望单独的处理元组中的元素
# 可以使用多个变量， 一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
gl_temp, gl_wetness = testmeasure()
print("温度是 %d" % gl_temp)
print("湿度是 %d" % gl_wetness)