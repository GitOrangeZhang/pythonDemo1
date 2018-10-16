#函数返回多个值
def info():
    a = 10
    b = 20
    return {'a1':a,'b1':b}

c = info()
print('返回的第一个值：'+str(c['a1']))
print('返回的第二个值：'+str(c['b1']))
