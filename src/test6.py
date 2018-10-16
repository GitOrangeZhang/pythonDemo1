#递归调用
def test1(num):
    if num>1:
        return num*test1(num-1)
    else:
        return 1

a = int(input('请输入阶乘计算的最大值：'))
result = test1(a)
print('1到'+str(a)+'之积为：'+str(result))

