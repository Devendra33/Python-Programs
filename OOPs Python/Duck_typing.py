# duck typing : we call function by object as an argument.
# object of any class in an exterior function.


def show(obj):  # this show() shows the duck typing.
    obj.fun()


class A:
   def __init__(self, a, str1):
       self.a  = a
       self.str1 = str1

   def fun(self):
        print(self.str1,'I am class A')

   def __str__(self):
    return f'a = {self.a} and str1 = {self.str1}'

class B:
    def __init__(self, a, str1):
        self.a = a
        self.str1 = str1

    def fun(self):
        print(self.str1,'I am class B')

    def __str__(self):
        return f'a = {self.a} and str1 = {self.str1}'

obj = A(10, 'hello')
print(obj)
show(obj)

obj1 = B(5,'hey')
show(obj1)
print(obj1)

