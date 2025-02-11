# 2025年01月05日
def homework_1(name,city = '',age = 18,gender = True):
    gender_str = '男生'
    if not gender:
        gender_str = '女生'

    print(f'{name}是{gender_str}，今年{age}岁，住在{city}。')




if __name__ == '__main__':
    homework_1('xiaoming','beijing',20)
    homework_1('zhangsan', age =21)

