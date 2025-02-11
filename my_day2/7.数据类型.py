def use_bool():
    print(True + 1)
    print(False + 1)


def use_complex():
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))


def use_hex():
    a = 123
    print(hex(a))
    print(bin(a))
    print(oct(a))


#use_bool()
#use_complex()
use_hex()
