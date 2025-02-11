# 2025年01月05日
def demo1(num, *args, **kwargs):
    print(f'demo1_{num}')
    print(f'demo1_{args}')
    print(f'demo1_{kwargs}')


def demo2(*args, **kwargs):
    demo1(1,*args,**kwargs)


if __name__ == '__main__':
    demo1(1, 2, 3, 4, 5, name='Alice', age=20)
    demo2(2, 3, 4, 5, name='Bob', age=30)
