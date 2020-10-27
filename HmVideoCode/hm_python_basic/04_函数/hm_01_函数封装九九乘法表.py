# 体验函数封装  --  九九乘法表

def multiple_table():

    row = 1

    while row <= 9:

        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, row*col), end="\t")
            col += 1

        print("")
        row += 1