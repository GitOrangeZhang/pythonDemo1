# 创建一个警察对象
class Police():
    def __init__(self,name):
        self.name = name
        self.bloodVolume = 100

    # 警察安装子弹的功能
    def installBullet(self,cartridgeClip,bullet):
        # 警察把子弹装进弹夹中
        cartridgeClip.saveBullets(bullet)

    # 警察安装弹夹的功能
    def installCartridgeClip(self,gun,cartridgeClip):
        # 警察把弹夹装到枪上
        gun.connectCartridgeClip(cartridgeClip)

# 创建一个弹夹对象
class CartridgeClip():
    def __init__(self,capacity):
        # 弹夹容量
        self.capacity = capacity
        # 装进去的子弹集合
        self.capacitys = []

    def __str__(self):
        return "弹夹中当前子弹数量为：" + str(len(self.capacitys)) + "/" + str(self.capacity)

    # 保存子弹的方法
    def saveBullets(self,bullet):
        # 如果弹夹没装满，就添加一个子弹
        if len(self.capacitys) < self.capacity:
            self.capacitys.append(bullet)

# 创建一个子弹对象
class Bullet():
    pass

# 创建一个枪对象
class Gun():
    def __init__(self):
        self.cartridgeClip = None

    def __str__(self):
        if self.cartridgeClip:
            return "枪有弹夹了，准备射击！"
        else:
            return "赶紧装弹夹，敌人马上来了！"

    def connectCartridgeClip(self,desertEagle,cartridgeClip):
        if not self.cartridgeClip:
            self.cartridgeClip = cartridgeClip

# 创建一个罪犯
class Offender():
    pass


# 创建一个警察
policeMan = Police("强森")

# 创建一个弹夹
cartridgeClip = CartridgeClip(20)
# print(cartridgeClip)

i = 0
while i<5:
# 创建一个子弹
    bullet = Bullet()
    policeMan.installBullet(cartridgeClip,bullet)
    i+=1
print(cartridgeClip)


# 创建一把枪
desertEagle = Gun()
# print(desertEagle)
desertEagle.connectCartridgeClip(desertEagle,cartridgeClip)
print(desertEagle)