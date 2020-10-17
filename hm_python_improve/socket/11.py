
def main():
    list1 = range(1,10)

    for i in list1:
        for j in range(1,i+1):

            mul = i * j
            if len(str(mul)) == 1:
                print('%d*%d=%d '% (j,i,mul) ,end='   ')
            else:
                print('%d*%d=%d' % (j, i, mul), end='   ')
        print('')



if __name__ == '__main__':
    main()