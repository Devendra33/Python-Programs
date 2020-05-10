class Cir:
    pi = 3.14
    def __init__(self,radius = 1):
        self.r = radius
    def area(self,str1):
        print(f'str1: {str1}')   # this parameter is passed from outside so,
                                 # we don't use (self.str1)
        return Cir.pi*self.r     # we use self.r bcoz r is reffered from constructor.
    def circum(self):
        return 2*Cir.pi*self.r
rad = int(input('Enter radius: '))
obj = Cir(rad)
str1 = "hello world"
print(f'area: {obj.area(str1):.2f}')
print(f'circumference: {obj.circum():.2f}')