class Cat:
    age = 1

    def __init__(self):
        self.name = 'bosi'

    def test(self):
        print(self.name)

    @classmethod
    def setAge(cls,newAge):
        cls.age = newAge

bosi = Cat()
print(bosi.name)

bosi.setAge(20)
print(Cat.age)