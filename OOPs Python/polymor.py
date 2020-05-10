# to demonstrate polymorphism.
class Cir:
    pi = 3.14
    def __init__(self, r = 1):
        self.r = r
        print("hello world")
    def area(self):
        return Cir.pi*self.r*self.r

class tst(Cir):
    def __init__(self):
        Cir.__init__(self)

c = tst()
print(f'{c.area()}')