# 2024年12月27日
def print_1():
    print("hello world")


def print_2(num):
    print("*"*num)


def print_3(key,num):
    print(key * num)


if __name__ == '__main__':
    print_1()
    print('-'* 50)
    print_2(50)
    print('-' * 50)
    print_3('abc',20)