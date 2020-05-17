class Test():
    '''To demonstrate the use of classmethod
        It basically acts on only class variables
        Calling format is classname.method()'''
    var = 10   # class variable
    wings = 2
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    @classmethod
    def wing(cls, bird):
        print(f'{bird} has {cls.wings} wings.')

    @classmethod
    def display(cls):
        cls.var += 10
        print(cls.var)
        # print(cls.name) #gives error bcoz name is instance variable.

    def show_instance(self):
        print(f'The name is {self.name} \n Age is {self.age}')

obj = Test('dev',20)
obj.show_instance()
Test.wing('Eagle')
Test.display()   # displays 20.
Test.display()   # displays 30.
Test.display()   # displays 40.
