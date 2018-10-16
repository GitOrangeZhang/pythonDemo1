#第一个函数
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第一个数字：'))
def sumNum(a,b):
    #计算两数之和
    c=a+b
    # print('%d+%d=%d'%(a,b,c))
    return c
d = sumNum(num1,num2)
print(d)
