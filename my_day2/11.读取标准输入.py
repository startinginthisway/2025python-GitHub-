def change_alpha():
    # 通过任务管理器查看程序卡在input还是死循环
    a = input('请输入内容')
    print(a)
    print(type(a))

    # 大小写转换
    print(chr(ord(a) + 32))


def change_type():
    a = input('请输入内容')
    c = int(a)
    print(c + 5)


change_type()
