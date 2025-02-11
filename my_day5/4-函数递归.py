# 2025年01月04日

# 所有递归都可以拆成循环，递归实现难度低（不建议调试递归）
# 1.找到递归公式
# 2.编写结束条件
import sys
sys.setrecursionlimit(10000)
def sum_numbers(num):
    print(num)
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)


def f(n):
    '''
    累加
    :param n:
    :return:
    '''
    # 结束条件
    if n == 1:
        return 1
    # 返回值
    return n + f(n - 1)


def step(n):
    '''
    如果有n 个台阶，每次只能走1 个，或者2 个台阶，到第n 个台阶有多少种走
法？
    :param n:
    :return:
    '''
    if n == 1 or n == 2:
        return n
    if n==3:
        return 4

    return step(n - 1) + step(n - 2)+ step(n - 3)


if __name__ == '__main__':
    # print(f(10))
    for i in range(1, 5):
        print(step(i))
