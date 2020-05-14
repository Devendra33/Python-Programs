# MRO : stands for METHOD RESOLUTION ORDER.
# object class No constructor.
# hybrid inheritance is not supported in python

class A(object):
    def __init__(self):
        print('A class.')
        super().__init__()
class B(object):
    def __init__(self):
        print('B class.')
        super().__init__()
class C(object):
    def __init__(self):
        print('C class')
        super().__init__()
class X(A, B):
    def __init__(self):
        print('X class.')
        super().__init__()
class Y(B, C):
    def __init__(self):
        print('Y class.')
        super().__init__()
class P(X, Y, C):
    def __init__(self):
        print('P class.')
        super().__init__()
obj = P()
# obj = Y()