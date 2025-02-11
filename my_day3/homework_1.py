# 2024年12月27日


import print_3

def find_only_num():
    my_list = [1,1,3,5,3,4,4]
    for i in my_list:
        num = my_list.count(i)
        if(num == 1):
            print(f'只出现了一次的数是{i}')


def print_num():
    for i in range(20):
        print('%d '%(i+1),end='')


def say_hello(num):
    print("Hello "*num)


def homework_5():
    num_list = [x for x in range(10)]
    name_list = ['张三','李四','王五']
    a = [11,12]
    # 增加
    num_list.insert(1,5)
    num_list.append(10)
    num_list.extend(a)
    print(num_list)
    # 修改
    num_list[1] = 1
    print(num_list)
    # 删除
    del num_list[11]
    print(num_list)
    num_list.remove(1)
    print(num_list)
    num_list.pop(10)
    print(num_list)
    num_list.clear()
    print(num_list)
    num_list.extend(a)
    # 统计
    print(len(num_list))
    print(num_list.count(12))
    print(num_list.index(12))
    # 排序
    num_list.sort()
    print(num_list)
    num_list.sort(reverse=True)
    print(num_list)
    num_list.reverse()
    print(num_list)


def homework_6():
    num_list = [1,2,4,8,10,2,10,4]
    for i in num_list:
        if(num_list.count(i)==1):
            print(f'只出现了一次的数为{i},在数列中的位置是{num_list.index(i)}')


# find_only_num()--

# print_num()

# say_hello(50)

# print_3.print_1()
# print('-'*60)
# print_3.print_2(50)
# print('-'*60)
# print_3.print_3('*-',50)

# homework_5()

homework_6()