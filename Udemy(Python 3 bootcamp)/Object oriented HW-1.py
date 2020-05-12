from math import sqrt
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
         print(f'{sqrt(((coor2[0] - coor1[0])**2)+((coor2[1] - coor1[1])**2)):.2f}')

    def slope(self):
        x = coor2[0] - coor1[0]
        y = coor2[1] - coor1[1]
        print(f'{y/x:.2f}')

coor1 = (3,2)
coor2 = (8,10)
L = Line(coor1,coor2)
L.distance()
L.slope()