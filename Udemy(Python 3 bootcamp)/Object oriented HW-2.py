class Cylinder():
    pi = 3.14

    def __init__(self,height = 1,radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        # V=πr2h
        print(f'{Cylinder.pi * self.height * (self.radius ** 2):.2f}')
    def surface_area(self):
        #A = 2πrh + 2πr2
        v1 = 2 * Cylinder.pi * self.radius * self.height
        v2 = 2 * Cylinder.pi * (self.radius ** 2)
        print(f'{v1 + v2 :.2f}')

c = Cylinder(2,3)
c.volume()
c.surface_area()