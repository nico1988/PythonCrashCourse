class Dog():
# class Dog(Object): #在Python 2.7中定义Dog 类时
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """
        self 是python自动植入的 属于指向实例自身的引用
        :param name:
        :param age:
        """
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting down")
    def rollOver(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog("xiaohua", 6)
my_mothoer_dog = Dog("xiaohuang",10)
my_dog.sit()
print(my_dog.name)
print(my_dog.age)
my_mothoer_dog.sit()