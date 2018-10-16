#不定长参数
def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

#test(1,'as',2,3,4,'qq',n=5,m='fg')

#可变与不可变
A = [1,2,3]
B = A
A.append(4)
print(A)
print(id(A))
print(B)
print(id(B))