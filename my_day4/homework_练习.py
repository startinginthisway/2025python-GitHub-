# 2025年01月02日
def homework_Tuple():
    '''
    不可修改变量类型
    :return:
    '''
    tuple1 = tuple([x for x in range(5)])
    tuple2 = ('xiaoming', 18, 1.8)
    print(tuple1.count(3))
    print(len(tuple1))
    print(tuple2[1])
    print(tuple2.index('xiaoming'))
    for i in tuple2:
        print(i)


def homework_dictionary():
    '''
    无序可变
    :return:
    '''
    my_dict = {'name': 'xiaoming', 'number': 12, 'age': 20}
    print(my_dict['name'])
    my_dict['age'] = 15
    my_dict.pop('name')
    for u, v in my_dict.items():
        print(f'{u}:{v}')
    print(my_dict)
    print(len(my_dict))
    temp_dict = {'height': 1.75}
    my_dict.update(temp_dict)
    print(my_dict)


def homework_char():
    '''
    不可变，顺序
    :return:
    '''
    s1 = 'abc*'
    for i in s1:
        print(i)
    print(s1.count('ab'))
    print(s1[2])
    print(s1.index('bc'))
    print(s1[1:3])
    # 查找替换
    s = 'abcdefgbcdefg'
    print(s.find('bc', 5))
    # 没有返回-1
    print(s.index('bc', 0))
    # 没有报错
    s2 = s.replace('cd', 'CD', s.count('cd'))
    print(s2)
    s1 = 'abc *** EFG'
    print(s1.split())
    print(type(s1.split()))
    s2 = s1.replace(' ', ',', 2)
    print(s2.split(','))
    str_list = ['a', 'b', 'c', 'd', 'e']
    print(str(str_list))
    str_al = ','.join(str_list)
    print(type(str_al))
    print(' '.join(str_list))
    print(str_al)
    # 分割
    num_str = "0123456789"
    print(num_str[2:6])
    print(num_str[2:])
    print(num_str[:6])
    print(num_str[:])
    print(num_str[::2])
    print(num_str[1::2])
    print(num_str[-1])
    print(num_str[2:-1])
    print(num_str[::-1])


def homework_set():
    '''
    无序，可变？去重
    :return:
    '''
    set1 = set()
    set2 = {1, 2, 3, 4, 5, 6}
    set2.add(7)
    x = set2.copy()
    print(x)
    print(id(x))
    print(id(set2))

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(z)
    # a = list(z)
    # print(a)
    # print(type(a))

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)

    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
    print(fruits)

    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    # 共有
    print(result)

    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    # 去交集

    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)
    # 并集

    print('apple' in z)
    # 存在

    print(x - y)
    print(x | y)
    print(x & y)
    print(x ^ y)




if __name__ == '__main__':
    homework_Tuple()
    print('*' * 50)
    homework_dictionary()
    print('*' * 50)
    homework_char()
    # print('\n')
    print('*' * 50)
    homework_set()
