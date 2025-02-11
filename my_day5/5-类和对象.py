# 2025年01月05日

# 类里面函数叫方法
# 对象时可变数据类型（即使没属性也是可变数据类型）
class person:
    def __init__(self, name, age, height):#多self
       self.name = name
       self.age = age
       self.height = height

    def run(self):
        '''
        调用方法
        :return:
        '''
        print(self.name + '正在跑步')

    def eat(self):
        print(self.name + '正在吃东西')

# 实例化
elephant = person('大象',18,1.75)
print(elephant.name,elephant.age,elephant.height)
elephant.run()
tiger = person('老虎',17,165)

print(dir(person))
print('*'*100)
print(dir(elephant))
print('*'*100)