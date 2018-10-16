#学生管理系统

stuInfos = [{'name':'张成1','gender':'男','age':'26'},{'name':'张成2','gender':'男','age':'27'},{'name':'张成3','gender':'男','age':'28'}]

# 打印菜单页面
def printMenu():
    print('*'*10+'欢迎进入学生管理系统'+'*'*10)
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查看学生信息')
    print('0.退出学生系统')
    print('*'*42)

#新增学生信息
def addStu():
    newName = input('请输入要添加的学生姓名：')
    newGnder = input('请输入要添加的学生性别：')
    newAge = input('请输入要添加的学生年龄：')
    stuInfo = {}
    stuInfo['name'] = newName
    stuInfo['gender'] = newGnder
    stuInfo['age'] = newAge
    stuInfos.append(stuInfo)
    print('添加成功！')
#删除学生信息
def delStu():
    xh = int(input('请输入要删除的学生序号：'))
    del stuInfos[xh-1]
    print('删除成功！')
#修改学生信息
def updateStu():
    xh = int(input('请输入要修改的学生序号：'))
    name = input('请输入修改后的学生姓名：')
    gender = input('请输入修改后的学生性别：')
    age = input('请输入修改后的学生年龄：')

    stuInfos[xh - 1]['name'] = name
    stuInfos[xh - 1]['gender'] = gender
    stuInfos[xh - 1]['age'] = age
    print('修改成功！')
#查看学生信息
def selectStu():
    print('序号\t\t姓名\t\t性别\t\t年龄')
    i = 1
    for tempStu in stuInfos:
        print(str(i)+'\t\t'+tempStu['name']+'\t\t'+tempStu['gender']+'\t\t'+tempStu['age'])
        i+=1
while True:
    printMenu()
    #获取用户选项
    key = input('请输入要操作的选项：')
    if key=='1':
        addStu()
    elif key=='2':
        delStu()
    elif key == '3':
        updateStu()
    elif key == '4':
        selectStu()
    elif key == '0':
        print('谢谢使用！')
        exit()
    else:
        print('对不起，请您输入正确的选项！')
