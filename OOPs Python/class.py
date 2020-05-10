# my first classs in python
class Dog():
    breed = 'mammal'    # class variable
    def __init__(self,name,age):   # constructor
        self.name = name
        self.age = age

obj = Dog('keshav',19)
obj1 = Dog('rohil',20)
print(f'Dog age: {obj1.age}')
print((f'breed: {Dog.breed}'))   # good practice to use class name for class variable.