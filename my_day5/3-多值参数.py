# 2025年01月04日
# 多值参数就是参数个数不确定
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, [1, 2, 3], 4, 5, name='小明', age=19)


# num删除
def demo1(*args, **kwargs):
    # print(num)
    print(args)
    print(kwargs)


demo1(1, 2, [1, 2, 3], 4, 5, name='小明', age=19)


# args参数必须在kwarge参数之前，不然报错


def demo2(*args, name='', age=''):
    '''
    可以但没人这样写
    :param args:
    :param name:
    :param age:
    :return:
    '''
    # print(num)
    print(args)
    print(name)
    print(age)


demo2(1, 2, [1, 2, 3], 4, 5, name='小明', age=19)


# 把demo4的传到demo3
# 继承传递形式（拆包）
def demo3(*args, **kwargs):
    print(f'demo3{args}')
    print(f'demo3{kwargs}')


def demo4(*args, **kwargs):
    print(args)
    print(kwargs)
    demo3(*args, **kwargs)  # 拆包,仅在函数传参过程中使用
    # args（未拆包），*args（拆包），kwagrs（未拆包），**kwagrs（拆包）
    # 不加*时args被看作一个变量，两个都不加星时会被看做两个整体的位置参数。


demo4(1, 2, [1, 2, 3], 4, 5, name='小明', age=19)
demo4()  # 可以不传参

a, b, c = (2, 3, 4)
