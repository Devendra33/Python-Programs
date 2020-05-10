class test(object):
    val = 10
    '''all variables and functions are public by default.'''
    def __init__(self, x, y):
        self.__x = x   # this is private variable
        self.y = y

    def show(self):
        print(self._test__x)  # accessing private variable inside class
        print(self.y)
t = test(15, 20)
t.show()
print(t._test__x) # accessing private variable from outside class.
                  # this is also known as name mangling.

