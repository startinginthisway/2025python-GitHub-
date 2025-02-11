# 2024年12月26日
#相加
def sun_2_num(num1, num2):
    """
    num1和num2是形参类型
    没有返回值时返回NONE判断为假
    :param num1:
    :param num2:
    :return:
    """
    result = num1 +num2
    print(f'求和结果是{num1 + num2}')
    return result


rec = sun_2_num('abc', 'efg')  # 3和5是实参
print(rec)


