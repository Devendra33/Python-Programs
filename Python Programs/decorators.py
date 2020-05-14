from math import sqrt
# to decorate function. gives sqrt of the returned value then multiply it by 10


def decor(fun):
    def inner():
        val = fun()
        return sqrt(val)
    return inner


def decor1(fun):
    def inner():
        val = fun()
        return val * 10
    return inner


def decor2(fun):
    def inner():
        val = fun()
        return val**2
    return inner


@decor1
@decor
def find_Sqrt():   # first @decor will work then @decor1 will work.
    return 9


print(find_Sqrt())


@decor2
def find_square():
    return 8


print(find_square())