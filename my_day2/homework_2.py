# 2024年12月25日
def use_int():
    a = 123
    print(a)
    print(type(a))


def use_float():
    a = 1.2345
    print(a)
    print(type(a))


def use_str():
    a = 'abc'
    print(a)
    print(type(a))


def use_bool():
    a = True
    print(a)
    print(type(a))


def use_complex():
    a = complex(1, 2)
    print("a是%d+%dj"%(a.real,a.imag))
    print(type(a))

use_str()
use_int()
use_float()
use_bool()
use_complex()